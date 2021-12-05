import psutil

def getExePath(proc):
	try:
		return proc.exe()
	except psutil.AccessDenied:
		return None

def printProcList():
	for proc in psutil.process_iter():
		if proc.pid == 0:
			continue
		path = getExePath(proc)
		if path is None:
			continue
		print(str(proc.pid) + ' : ' + path)

printProcList()
