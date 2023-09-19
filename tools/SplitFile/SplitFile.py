import sys

def getFNSub(fnBase, suffix):
	i = fnBase.rfind('.')
	if i != -1:
		return fnBase[0:i] + '_' + suffix + fnBase[i:]
	else:
		return fnBase + '_' + suffix

def mainproc(file):
	with open(file) as f:
		v = f.read().splitlines()
		n = len(v)
		hn = n // 2 + n % 2
		fna = getFNSub(file, 'A')
		fnb = getFNSub(file, 'B')
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
