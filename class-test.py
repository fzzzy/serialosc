import os, sys, time, random, fnmatch
import threading

sys.path.append('./profiles/')

deviceList = {}
deviceNames = []

for n in os.listdir("profiles/"):
	if fnmatch.fnmatch(n, '*.py'):
		if n != '__init__.py':
			deviceNames.append(n[0:-3])

print "found devices: %s" % deviceNames

devices = map(__import__, deviceNames)

for n in devices:
	m = n.identify()
	deviceList[m[0]] = m[1]
		
if __name__ == "__main__":
	a = deviceList["m64"]("instance a ++")
	b = deviceList["m64"]("instance b ++++")
	c = deviceList["m64"]("instance c ++++++")
	d = deviceList["m40h"]("instance d ++++++++")
	
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		pass
