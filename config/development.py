from portolano.store import filesystem

DEBUG = True

UPLOAD_FOLDER = 'charts'
STORE = filesystem

filesystem.init(UPLOAD_FOLDER)


