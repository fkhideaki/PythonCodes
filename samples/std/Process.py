import psutil
import subprocess

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

def findProcByPath(filePath):
	for proc in psutil.process_iter():
		if proc.pid == 0:
			continue
		path = getExePath(proc)
		if path == filePath:
			return proc
	return None

def openDirExplorer(dir):
	subprocess.Popen(['explorer', dir], shell=True)

def restartProc(filePath):
	p = findProcByPath(filePath)
	if not p is None:
		p.kill()
	subprocess.Popen(filePath)
