
from flask import (
    request,
)
from werkzeug.utils import secure_filename


def post(chart):

    f = request.files['file']
    if f:
        filename = secure_filename(f.filename)
        f.save(filename)
    return {"url": "http://foo"}, 200
