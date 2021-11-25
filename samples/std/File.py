import os
import shutil

def printFilesInDir(dirpath):
    files = os.listdir(dirpath)
    for f in files:
        fp = os.path.join(dirpath, f)
        print(fp)
