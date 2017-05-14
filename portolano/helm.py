import contextlib
import os
import shutil
import subprocess
import tarfile


@contextlib.contextmanager
def pushd(path):
    curdir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(curdir)

# TODO validate that helm is available in the PATH


def process(chart_path, url):

    dirname = os.path.dirname(chart_path)
    chart_name = os.path.basename(chart_path)

    with pushd(dirname):

        # generate index
        subprocess.run(["helm", "repo", "index", "--url", url, '.'], check=True)

        # Make name unique
        index_path = os.path.join(dirname, chart_name + '.index.yaml')
        shutil.copyfile('index.yaml', index_path)

        return index_path

