import os

def indexToStr(idx, len):
	return ('0' * len + str(idx))[-len:]

def dirp(obj):
    """非公開をメンバ一覧"""
    a = []
    for s in dir(obj):
        if s.startswith('__'): continue
        if s.endswith('__'): continue
        a.append(s)
    return a

class CurrentDir:
	def __init__(self, wsDir):
		self.iniDir = os.getcwd()
		self.wsDir = wsDir

	def __enter__(self):
		os.chdir(self.wsDir)
		return self

	def __exit__(self, exception_type, exception_value, traceback):
		os.chdir(self.iniDir)
