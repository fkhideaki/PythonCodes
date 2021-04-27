def z4(i):
    s = '0' * 4 + str(i)
    return s[-4:]

def makeCmd(src, dst):
    s = 'move'
    s += ' ' + z4(src) + '.png'
    s += ' ' + z4(dst) + '.png'
    return s

def callRename(maxSrc, pitch, offSrc, offDst):
    i = 1
    while True:
        src = offSrc + i * pitch
        dst = offDst + i
        i += 1
        print(makeCmd(src, dst))
        if src >= maxSrc:
            break

maxSrc = 976
pitch = 3
offSrc = 1
offDst = 1
callRename(maxSrc, pitch, offSrc, offDst)
