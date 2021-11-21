import requests

def getFN(url):
	return url.split('/')[-1]

def downloadFile(url, fn):
	urlData = requests.get(url).content
	with open(fn, mode='wb') as f:
		f.write(urlData)

def downloadFileA(url):
	fn = getFN(url)
	downloadFile(url, fn)

def indexToStr(idx, len):
	return ('0' * len + str(idx))[-len:]

def downloadIntAry(urlBase, i0, i1, il):
	for i in range(i0, i1 + 1):
		if il == 0:
			s = str(i)
		else:
			s = indexToStr(i, il)
		url = urlBase.replace('##IDX##', s)
		print(url)
		downloadFileA(url)

#downloadIntAry('https://aaa.bbb.ccc/##IDX##.jpg', 59, 92, 2)