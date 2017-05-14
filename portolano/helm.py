import os
import shutil
import subprocess


# TODO validate that helm is available in the PATH

def process(chart_path, url):

    # generate index
    subprocess.run(["helm", "repo", "index", "--url", url, '.'], check=True)

    # Make name unique
    chart_name = os.path.basename(chart_path)
    index_name = chart_name + ".index.yaml"
    shutil.copyfile('index.yaml', index_name)

    return index_name

