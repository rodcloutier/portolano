import contextlib
import os
import tempfile

from flask import (
    request,
)
from werkzeug.utils import secure_filename

from portolano import (
    app,
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


def post(chart):

    f = request.files['file']
    if f:
        filename = secure_filename(f.filename)
        with tempfile.TemporaryDirectory() as tmp_dir:
            with pushd(tmp_dir):

                archive_path = os.path.join(tmp_dir, filename)
                f.save(archive_path)

                storage = app.config["STORAGE"]
                url = storage.base_url
                indexname = helm.process(archive_path, url)
                if not indexname:
                    return "Failed to create index for chart", 500

                storage.save(f, filename)
                storage.save(open(indexname, 'rb'), indexname)

        return {"url": storage.url(filename)}, 200

    return "missing file", 400


