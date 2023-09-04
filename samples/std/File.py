import os
import glob

def printFilesInDir(dirpath):
    files = os.listdir(dirpath)
    for f in files:
        fp = os.path.join(dirpath, f)
        print(fp)

def printFilesInDirGlob(dirpath):
    files = glob.glob(dirpath + '*.*')
    for f in files:
        print(f)

def getAllLines(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()
