import collections

import yaml


# To remove the args and extra fields from defaultdict in yaml output
from yaml.representer import Representer
yaml.add_representer(collections.defaultdict, Representer.represent_dict)


def generate(storage):

    # TODO generate barebone index with helm

    all_entries = collections.defaultdict(list)

    for f in storage.list_files():
        if f.endswith('index.yaml'):
            content = yaml.load(storage.read(f))
            for name, entries in content['entries'].items():
                all_entries[name].extend(entries)

    index = {
        "apiVersion": "v1",
        "entries": all_entries
    }
    return yaml.dump(index)

