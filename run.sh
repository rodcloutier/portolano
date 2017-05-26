export DEBUG=1
gunicorn --config config/gunicorn_config.py portolano:connexion_app
