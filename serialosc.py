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

if __name__ == "__main__":
	
	incoming_bytes = []
	portList = []
	connected = False
	ser = serial.Serial()

	print "==========serialosc ====================================="
	print "========= ctrl-c to quit ================================"

	def register_callback(sdRef, flags, errorCode, name, regtype, domain):
	    if errorCode == pybonjour.kDNSServiceErr_NoError:
	        print 'Registered service:'
	        print '  name    =', name
	        print '  regtype =', regtype
	        print '  domain  =', domain

	name    = 'serialosc/m64-0001'
	regtype = '_osc._udp'
	port    = 8080

	sdRef = pybonjour.DNSServiceRegister(name = name,
	                                     regtype = regtype,
	                                     port = port,
	                                     callBack = register_callback)
	
	c = OSCClient()
	try:
		c.connect(('0.0.0.0', 8000))
	except OSC.OSCClientError:
		pass
	
	
	def printing_handler(addr, tags, stuff, source):
		msg_string = "%s [%s] %s" % (addr, tags, str(stuff))
		sys.stdout.write("OSCServer Got: '%s' from %s\n" % (msg_string, getUrlStr(source)))
		return
	
	def sys_port_handler(addr, tags, stuff, source):
		try:
			c.connect(('0.0.0.0', stuff[0]))
			print "port switched to %d" % stuff[0]
		except OSC.OSCClientError:
			pass
		return
		
	def led_handler(addr, tags, stuff, source):
		try:
			x = stuff[0]
			y = stuff[1]
			state = stuff[2]
			
			a = (abs(state-1)+2) << 4
			b = (x << 4) + y
			ser.write(chr(a) + chr(b))
			print "OSC received, serial written: %10s %10s" % (bin(a), bin(b))
		except IOError:
			print "serial write error?"
		return
	
	s = OSCServer(('0.0.0.0', 8080))
	s.addDefaultHandlers()
	s.addMsgHandler("/print", printing_handler)
	s.addMsgHandler("/sys/port", sys_port_handler)
	s.addMsgHandler("/led", led_handler)
	st = threading.Thread(target=s.serve_forever)
	st.start()
	print "Starting OSCServer."
		
	
########################### main loop ##################################	
	try:
		ready = select.select([sdRef], [], [])
		if sdRef in ready[0]:
			pybonjour.DNSServiceProcessResult(sdRef)
			
		while True:
			
			if not connected:
				portList = []
				for port in os.listdir("/dev/"):
					if ('m64' or 'm128' or 'm256') and 'tty.usb' in port:
						devFile = os.path.normpath(os.path.join("/dev", port))
						portList.append(devFile)
				
				if len(portList)>0:
					print "found %d monome device" % len(portList)
					try:
						ser = serial.Serial(portList[0],57600)
						connected = True
						print "connected to %s" % devFile
					except serial.serialutil.SerialException:
						print "port busy, will try again..."
				
			else:
				try:	
					while ser.inWaiting():
						incoming_bytes.append(ser.read())
						if len(incoming_bytes) == 2:
							m = OSCMessage()
							t = ord(incoming_bytes[0]) >> 4
							
							if (t == 0) or (t == 1):
								x = ord(incoming_bytes[1]) >> 4
								y = ord(incoming_bytes[1]) & 0x0f
								m.setAddress("/press")
								m.append(x)
								m.append(y)
								m.append(abs(t-1))
								try:
									c.send(m)
								except OSCClientError:
									pass
							print "serial received: %10s %10s" % (bin(ord(incoming_bytes[0])), bin(ord(incoming_bytes[1])))
							incoming_bytes = []				
				except IOError:
					print "device disconnected"
					connected = False
				
			
			time.sleep(0.01)
			
	except KeyboardInterrupt:
		pass
	
	if connected:
		ser.close()
		s.close()
		st.join()
		c.close()