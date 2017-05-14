import os


SETTINGS = {}


def init(directory):
    SETTINGS['directory'] = directory


def persist(filestorage, filename):
    filestorage.save(os.path.join(SETTINGS['directory'], filename))
