import os

def getMyDir():
    return os.path.dirname(__file__)

def getAbsPath(path):
    return os.path.abspath(path)
