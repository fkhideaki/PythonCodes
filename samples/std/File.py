import os

def printFilesInDir(dirpath):
    for f in os.listdir(dirpath):
        fp = os.path.join(dirpath, f)
        print(fp)

printFilesInDir('.')
