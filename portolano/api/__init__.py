
from flask import (
    Response,
    request,
)
from flask import current_app as app

from portolano import (
    index
)


def get(filename):
    if filename != "index.yaml":
        return "File not found", 404

    content = index.generate(app.config['STORAGE'])

    return Response(content,
                    mimetype="text/plain",
                    headers={"Content-disposition": "attachment;filename=index.yaml"})

