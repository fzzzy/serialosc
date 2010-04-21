import sys
import time
import threading

import serial
import pybonjour
from OSC import *

class MonomeSeries(object):
	"""launch/maintain monome devices"""
	
	def __init__(self, path):
		print "device: monomeseries init"
		self.ser = serial.Serial()
		self.osc_client = OSCClient()
		self.alive = False
		self.path = path
		self.name = path[19:]
		self.th = threading.Thread(target=self.main)
		self.th.start()

	# osc handlers ###############################################
	
	def printing_handler(self, addr, tags, stuff, source):
		msg_string = "%s [%s] %s" % (addr, tags, str(stuff))
		sys.stdout.write("osc: '%s' from %s\n" % (msg_string, getUrlStr(source)))
		return
	
	def sys_port_handler(self, addr, tags, stuff, source):
		try:
			self.osc_client.connect(('0.0.0.0', stuff[0]))
			print "osc: port switched to %d" % stuff[0]
		except OSC.OSCClientError:
			pass
		return
		
	def led_handler(self, addr, tags, stuff, source):
		try:
			x = stuff[0]
			y = stuff[1]
			state = stuff[2]
			
			a = (abs(state-1)+2) << 4
			b = (x << 4) + y
			self.ser.write(chr(a) + chr(b))
			print "OSC received, serial written: %10s %10s" % (bin(a), bin(b))
		except IOError:
			print "serial write error?"
			self.alive = False
		return
	

	# main ############################################################

	def main(self):
		print "%s: main loop started" % self.name
		
		retry = 4
		while retry > 0:
			try:
				self.ser = serial.Serial(self.path,115200)
				print "%s: connected to %s" % (self.name, self.path)
				self.alive = True
				retry = 0
			except serial.serialutil.SerialException:
				print "%s: port busy, will try again..." % self.name
				retry = retry - 1
			time.sleep(1)
		
		if self.alive:	
			try:
				self.osc_client.connect(('0.0.0.0', 8000))
			except OSC.OSCClientError:
				print "no destination port?"
			
			
			# Passing 0 chooses a random, unused port
			self.osc_server = OSCServer(('0.0.0.0', 0))
			listen_port = self.osc_server.socket.getsockname()[1]
			#print "OSC Server listening on %s" % listen_port
			self.osc_server.addDefaultHandlers()
			self.osc_server.addMsgHandler("/print", self.printing_handler)
			self.osc_server.addMsgHandler("/sys/port", self.sys_port_handler)
			self.osc_server.addMsgHandler("/led", self.led_handler)
			self.osc_server_thread = threading.Thread(\
										target=self.osc_server.serve_forever)
			self.osc_server_thread.start()
			print "%s: starting OSC server" % self.name


			def register_callback(sdRef, flags, errorCode, name, regtype, domain):
			    if errorCode == pybonjour.kDNSServiceErr_NoError:
			        print 'Registered service:'
			        print '  name    =', name
			        print '  regtype =', regtype
			        print '  domain  =', domain

			# TODO: what happens if this registration fails? can it fail?
			sdRef = pybonjour.DNSServiceRegister(name = "serialosc/"+self.name,
			                                     regtype = '_osc._udp',
			                                     port = listen_port,
			                                     callBack = register_callback)

			ready = select.select([sdRef], [], [])
			if sdRef in ready[0]:
				pybonjour.DNSServiceProcessResult(sdRef)

			incoming_bytes = []

			while self.alive is True:
				try:	
					while self.ser.inWaiting():
						incoming_bytes.append(self.ser.read())
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
									self.osc_client.send(m)
								except OSCClientError:
									pass
							print "serial received: %10s %10s" % (bin(ord(incoming_bytes[0])), bin(ord(incoming_bytes[1])))
							incoming_bytes = []				
				except IOError:
					print "%s: device disconnected" % self.name
					self.alive = False
				time.sleep(0.001)
			
			print "%s: time to stop" % self.name
			self.ser.close()
			print "%s: serial port closed" % self.name
			self.osc_client.close()
			self.osc_server.close()
			self.osc_server_thread.join()
			print "%s: osc server closed" % self.name
			
		print "%s: main loop finished" % self.name
		
	def close(self):
		self.alive = False
		
				

def identify():
	""" search string in /dev to identify device associated with this class"""
	return ("m64", MonomeSeries)


if __name__ == "__main__":
	c = MonomeSeries("/dev/tty.usbserial-m64-0001")

	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		c.close()