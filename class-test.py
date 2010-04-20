"""
bonjour-enabled serial router using open sound control
"""

import sys
import os
import time

sys.path.append('./profiles/')


# scan profiles/ for available device profiles

device_list = {}
device_names = []

for n in os.listdir("profiles/"):
	if n.endswith('.py'):
		if n != '__init__.py':
			device_names.append(n[0:-3])

print "found devices: %s" % device_names

devices = map(__import__, device_names)

for n in devices:
	m = n.identify()
	device_list[m[0]] = m[1]


		
if __name__ == "__main__":
	a = device_list["m64"]("instance a ++")
	b = device_list["m64"]("instance b ++++")
	c = device_list["m64"]("instance c ++++++")
	d = device_list["m40h"]("instance d ++++++++")
	
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		pass
