import connexion
from connexion.resolver import RestyResolver
import os.path


UPLOAD_FOLDER = "charts"

specification_dir = os.path.join(os.path.dirname(__file__), 'api')

app = connexion.App(__name__, specification_dir='api/')

app.add_api('api.yaml', resolver=RestyResolver('api'))

app.run(port=8080)

