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


def post(chart):

    f = request.files['file']
    if f:
        filename = secure_filename(f.filename)
        with tempfile.TemporaryDirectory() as tmp_dir:
            archive_path = os.path.join(tmp_dir, filename)
            f.save(archive_path)
            url = app.config["STORE"].persist(archive_path)
            index_path = helm.process(archive_path, url)
            if not index_path:
                return "Failed to create index for chart", 500
            url = app.config["STORE"].persist(index_path)
        return {"url": url}, 200

    return "missing file", 400


