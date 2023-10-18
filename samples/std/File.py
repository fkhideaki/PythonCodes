import os
import glob
import shutil

def moveFile(src, dst):
    os.rename(src, dst)

def copyFile(src, dst):
    shutil.copy2(src, dst)

def isFileExists(fp):
    return os.path.isfile(fp)

def isDirExists(fp):
    return os.path.isdir(fp)

def isPathExists(fp):
    return os.path.exists(fp)

# recursive
def makeDir(fp):
    os.makedirs(fp)

def delFile(fp):
    os.remove(fp)

#recursive
def delDir(fp):
    shutil.rmtree(fp)

#recursive
def copyDir(src, dst):
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

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
