
from flask import (
    Response,
)

from portolano import (
    app,
    index
)


def get(filename):
    print(filename)
    if filename != "index.yaml":
        return "File not found", 404

    content = index.generate(app.config['STORAGE'])

    return Response(content,
                    mimetype="text/plain",
                    headers={"Content-disposition": "attachment;filename=index.yaml"})

