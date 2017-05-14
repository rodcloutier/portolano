
from flask import (
    request,
)
from werkzeug.utils import secure_filename


def post(chart):

    f = request.files['file']
    if f:
        filename = secure_filename(f.filename)
        app.config["STORE"].persist(f, filename)
        return {"url": "http://foo"}, 200

    return "missing file", 400


