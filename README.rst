===============
portolano
===============

Simple Helm repository server backed with object storage.
The Italian adjective portolano means "related to ports or harbors" or "a collection of sailing directions".

Currently supports the following backends (provided by `flask-fs<https://github.com/noirbizarre/flask-fs>`_

- S3
- Swift
- Gridfs
- local filesystem


Installation
============

.. code-block:: console

    $ docker run --rm -ti -p 5000:5000 --name portolano rodcloutier/portolano:latest



Configuration
=============

portolano uses flask-fs. To use a specific backend, use the

FS_BACKEND configuration to select it. See `flask-fs configurations<http://flask-fs.readthedocs.io/en/latest/config.html>`_

FLASK_FS_OVERWRITE Will allow to overwrite the uploaded files (false by default)

It also uses flask-env, so all configuration is set using environment variables.

Development
================

local
-----

For development

.. code-block:: console

    $ export FLASK_APP=portolano
    $ export DEBUG=1
    $ export FLASK_FS_OVERWRITE=1
    $ export FS_LOCAL_ROOT=$PWD/instance
    $ flask run


Running gunicorn

.. code-block:: console

    $ export FLASK_APP=portolano
    $ export DEBUG=1
    $ export FLASK_FS_OVERWRITE=1
    $ export FS_LOCAL_ROOT=$PWD/instance
    $ gunicorn --config config/gunicorn_config.py portolano:connexion_app


docker
------

.. code-block:: console

    $ docker build -t portolano .
    $ docker run --rm -ti -p 5000:5000 --name portolano portolano


