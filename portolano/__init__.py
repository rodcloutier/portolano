import os

import connexion
from connexion.resolver import RestyResolver

specification_dir = os.path.join(os.path.dirname(__file__), 'api')

connexion_app = connexion.App(__name__, specification_dir='api/')
app = connexion_app.app

# Load the default configuration
app.config.from_object('config.default')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
app.config.from_envvar('PORTOLANO_CONFIG_FILE')

connexion_app.add_api('api.yaml', resolver=RestyResolver('portolano.api'))

