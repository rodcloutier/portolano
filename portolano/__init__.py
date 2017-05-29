import os

import connexion
from connexion.resolver import RestyResolver
from flask_env import MetaFlaskEnv
import flask_fs


def portolano():

    class Configuration(metaclass=MetaFlaskEnv):
        DEBUG = False
        PORT = 5000
        FLASK_FS_OVERWRITE = False

        # Flask fs shared configuration
        FS_LOCAL_ROOT = os.getcwd()  # The file system root

        FS_S3_ENDPOINT = None  # The S3 API endpoint
        FS_S3_REGION = None  # The region to work on.
        FS_S3_ACCESS_KEY = None  # The AWS credential access key
        FS_S3_SECRET_KEY = None  # The AWS credential secret key

        FS_GRIDFS_MONGO_URL = None  # The Mongo access URL
        FS_GRIDFS_MONGO_DB = None  # The database to store the file in.

        FS_SWIFT_AUTHURL = None  # The Swift Auth URL
        FS_SWIFT_USER = None  # The Swift user in
        FS_SWIFT_KEY = None  # The user API Key

        # Back end selection
        CHARTS_FS_BACKEND = 'local'
        CHARTS_FS_URL = "http://127.0.0.1:5000"

    specification_dir = os.path.join(os.path.dirname(__file__), 'api')

    connexion_app = connexion.App(__name__, specification_dir='api/')
    # Connexion initializtion
    connexion_app.add_api('api.yaml', resolver=RestyResolver('portolano.api'))
    app = connexion_app.app

    # Load the configuration from env var
    app.config.from_object(Configuration)

    # Storage initialization
    flask_fs.init_app(app)
    app.config['STORAGE'] = flask_fs.Storage(
        'charts',
        ('tar', 'tgz'),
        overwrite=app.config['FLASK_FS_OVERWRITE']
    )
    app.config['STORAGE'].configure(app)
    return app

app = portolano()



