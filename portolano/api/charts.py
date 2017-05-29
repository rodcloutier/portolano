import contextlib
import os
import tempfile

from flask import (
    request,
)
from flask import current_app as app

from portolano import (
    helm
)


@contextlib.contextmanager
def pushd(path):
    curdir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(curdir)


def post():

    f = request.files['file']
    with tempfile.TemporaryDirectory() as tmp_dir:
        with pushd(tmp_dir):

            filename = os.path.basename(f.filename)
            f.save(filename)

            storage = app.config["STORAGE"]
            url = storage.base_url
            indexname = helm.process(filename, url)
            if not indexname:
                return "Failed to create index for chart", 500

            storage.save(f, filename)
            with open(indexname, 'rb') as index_file:
                storage.save(index_file, indexname)

    return {"url": storage.url(filename)}, 200


