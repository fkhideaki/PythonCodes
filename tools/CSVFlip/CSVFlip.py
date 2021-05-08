import sys

def getF(fn):
	vl = []
	with open(fn) as f:
		fl = f.read().splitlines()
		for l in fl:
			vl.append(l.split(','))
	return vl

def makeFlip(fn, vl):
	nl = len(vl)
	ni = len(vl[0])
	rm = []
	for j in range (ni):
		rv = []
		for i in range (nl):
			rv.append(vl[i][j])
		rm.append(rv)
	return rm

def printFlip(fn, rm):
	print('--------------------------------')
	print(fn)
	print('--------------------------------')
	for l in rm:
		print(l)
	print('--------------------------------')
	print('')

def procFile(fn):
	vl = getF(fn)
	if len(vl) == 0:
		print('empty : ' + fn)
		return
	rm = makeFlip(fn, vl)
	printFlip(fn, rm)

for f in sys.argv:
	if f is sys.argv[0]:
		continue
	procFile(f)
