import sys

def getFNSub(fnBase, suf):
	vs = fnBase.split('.')
	r = ''
	for s in vs:
		if s is vs[-1]:
			r += '_' + suf
		if not s is vs[0]:
			r += '.'
		r += s
	return r

def mainproc(file):
	with open(s) as f:
		v = f.read().splitlines()
		n = len(v)
		hn = n // 2 + n % 2
		fna = getFNSub(s, 'A')
		fnb = getFNSub(s, 'B')
		with open(fna, mode='w') as fo:
			for i in range(0, hn):
				fo.write(v[i] + '\n')
		with open(fnb, mode='w') as fo:
			for i in range(hn, n):
				fo.write(v[i] + '\n')

for s in sys.argv:
	if s is sys.argv[0]:
		continue
	mainproc(s)
