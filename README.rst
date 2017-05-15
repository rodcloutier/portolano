===============
portolano
===============

Simple Helm repository server backed with object storage.
The word portolan comes from the Italian adjective portolano, meaning "related to ports or harbors", or "a collection of sailing directions".

Currently supports the following backends (provided by `flask-fs<https://github.com/noirbizarre/flask-fs>`_

- S3
- Swift
- Gridfs
- local filesystem


Installation
============

.. code-block:: console

    $ docker run --rm -ti -p 5000:5000 -e PORTOLANO_CONFIG_FILE=/config/prod.config -v /$PWD/config.prod:/config --name portolano rodcloutier/portolano:latest



Configuration
=============

portolano uses flask-fs. To use a specific backend, use the

FS_BACKEND configuration to select it. See `flask-fs configurations<http://flask-fs.readthedocs.io/en/latest/config.html>`_

FLASK_FS_OVERWRITE Will allow to overwrite the uploaded files (false by default)


Development
================

local
-----

For development

.. code-block:: console

    $export FLASk_APP=portolano
    $ export PORTOLANO_CONFIG_FILE=/path/to/config/file
    $ flask run


Running gunicorn

.. code-block:: console

    $ export FLASk_APP=portolano
    $ export PORTOLANO_CONFIG_FILE=/path/to/config/file
    $ gunicorn --config config/gunicorn_config.py portolano:connexion_app


docker
------

.. code-block:: console

    $ docker build -t portolano -f Dockerfile.dev .
    $ docker run --rm -ti -p 5000:5000 -e PORTOLANO_CONFIG_FILE=/config/prod.config -v /$PWD/config.prod:/config --name portolano portolano


