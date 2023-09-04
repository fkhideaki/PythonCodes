import gzip

def makeGZip(src, dst):
    with open(src, mode='rb') as f:
        with gzip.open(dst, mode='wb') as z:
            shutil.copyfileobj(f, z)
