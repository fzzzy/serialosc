"""
bonjour-enabled serial router using open sound control
"""

import sys
import time
import os
import threading

import serial
import pybonjour
from OSC import *

sys.path.append('./profiles/')

if __name__ == "__main__":

	found_ports = []
	used_ports = []
	open_devices = {}

	print "==========serialosc ====================================="
	print "========= ctrl-c to quit ================================"
		
	# scan profiles/ for available device profiles

	device_list = {}
	device_names = []

	for n in os.listdir("profiles/"):
		if n.endswith('.py'):
			if n != '__init__.py':
				device_names.append(n[0:-3])

	print "found devices profiles: %s" % device_names

	devices = map(__import__, device_names)

	for n in devices:
		m = n.identify()
		device_list[m[0]] = m[1]	
	
	
	# main loop ##################################	
	try:			
		while True:			
			found_ports = []
			for port in os.listdir("/dev/"):
				if ('m64' in port or 'm128' in port or 'm256' in port) and 'tty.usb' in port:
				 	matched_port = os.path.normpath(os.path.join("/dev", port))
					found_ports.append(matched_port)
			
			for n in found_ports:
				if n not in used_ports:
					used_ports.append(n)
					print "opening: %s" % n
					open_devices[n] = device_list["m64"](n)
					print "opened: %s" % n
						
			# check for device removal, mod used_ports
				
				
			# how often to rescan?
			time.sleep(1)
			
	except KeyboardInterrupt:
		for m, n in open_devices.items():
			print "closing %s" % m
			n.close()
			print "successfully closed %s" % m