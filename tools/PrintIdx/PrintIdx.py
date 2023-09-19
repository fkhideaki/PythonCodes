
def idx(valLen, val):
    return ('0' * valLen + str(val))[-valLen:]

valLen = 3

def printIdxAry(i0, i1):
    for i in range(i0, i1 + 1):
        print(idx(valLen, i))

printIdxAry(2, 5)
