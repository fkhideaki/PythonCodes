
def getAllLines(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()
