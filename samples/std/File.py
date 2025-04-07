import os
import glob
import shutil
import pathlib

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

def makeDir(fp):
    """recursive"""
    os.makedirs(fp)

def delFile(fp):
    os.remove(fp)

def delDir(fp):
    """recursive"""
    shutil.rmtree(fp)

def copyDir(src, dst):
    """recursive"""
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

def getParentDir(path):
    return pathlib.Path(path).parent

def getFilename(path):
    return os.path.basename(path)

def getFilenameWithoutExt(path):
    os.path.splitext(os.path.basename(path))[0]
