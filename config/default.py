from portolano.store import filesystem

DEBUG = False

UPLOAD_FOLDER = 'charts'
STORE = filesystem

filesystem.init(UPLOAD_FOLDER)


