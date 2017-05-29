import os
import shutil
import subprocess


# TODO validate that helm is available in the PATH

def process(chart_name, url):

    # generate index
    subprocess.run(["helm", "repo", "index", "--url", url, '.'], check=True)

    # Make name unique
    index_name = chart_name + ".index.yaml"
    shutil.copyfile('index.yaml', index_name)

    return index_name

