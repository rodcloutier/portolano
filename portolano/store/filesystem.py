import os
import shutil

SETTINGS = {}


def init(directory):
    SETTINGS['directory'] = directory


def persist(filepath):

    filename = os.path.basename(filepath)
    shutil.copyfile(filepath, os.path.join(SETTINGS['directory'], filename))
    return "http://foo"
