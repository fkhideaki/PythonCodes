def indexToStr(idx, len):
	return ('0' * len + str(idx))[-len:]

class CurrentDir:
	def __init__(self, wsDir):
		self.iniDir = os.getcwd()
		self.wsDir = wsDir

	def __enter__(self):
		os.chdir(self.wsDir)
		return self

	def __exit__(self, exception_type, exception_value, traceback):
		os.chdir(self.iniDir)
