from urllib import request
import requests
import traceback

def getFN(url):
	fnb = url.split('/')[-1]
	fnb = fnb.split('?')[0]
	return fnb

def downloadFile(url, fn):
	urlData = requests.get(url).content
	with open(fn, mode='wb') as f:
		f.write(urlData)

def downloadFileA(url):
	fn = getFN(url)
	downloadFile(url, fn)

def indexToStr(idx, len):
	return ('0' * len + str(idx))[-len:]

def downloadIntAry(urlBase, i0, i1, indexLen):
	for i in range(i0, i1 + 1):
		if indexLen == 0:
			s = str(i)
		else:
			s = indexToStr(i, indexLen)
		url = urlBase.replace('##IDX##', s)
		print(url)
		downloadFileA(url)

def downloadStr(url):
	try:
		u = request.urlopen(url)
		return u.read()
	except Exception as err:
		print(err)
		return None

#downloadIntAry('https://aaa.bbb.ccc/##IDX##.jpg', 59, 92, 2)
