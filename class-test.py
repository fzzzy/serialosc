import os, sys, time, random
import threading

# from profiles.monomedevice import *
# from profiles.m2 import *

deviceList = []

for n in os.listdir("profiles/"):
	deviceFile = os.path.normpath(os.path.join("profiles/", n))
	deviceList.append(deviceFile)

print deviceList

devices = []

for n in deviceList:
	devices.append(__import__(n))

	
DeviceList = {"md":MonomeDevice, "m2":devices[0].m2.m2}
	
if __name__ == "__main__":
	a = DeviceList["md"]("m1")
	b = DeviceList["m2"]("+++++++++++")
	c = MonomeDevice("m3")
	d = MonomeDevice("m4")
	
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		pass
