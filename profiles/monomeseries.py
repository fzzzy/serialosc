import sys
import time
import threading

import pybonjour
from OSC import *

class MonomeSeries(object):
	"""launch/maintain monome devices"""
	
	def __init__(self):
		print "init"
		self.alive = True
		self.th = threading.Thread(target=self.main)
		self.th.start()

	
	def printing_handler(self, addr, tags, stuff, source):
		msg_string = "%s [%s] %s" % (addr, tags, str(stuff))
		sys.stdout.write("OSCServer Got: '%s' from %s\n" % (msg_string, getUrlStr(source)))
		return
	
	def sys_port_handler(self, addr, tags, stuff, source):
		try:
			#c.connect(('0.0.0.0', stuff[0]))
			print "port switched to %d" % stuff[0]
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
			#ser.write(chr(a) + chr(b))
			print "OSC received, serial written: %10s %10s" % (bin(a), bin(b))
		except IOError:
			print "serial write error?"
		return
	


	def main(self):
		print "main"
		self.s = OSCServer(('0.0.0.0', 8080))
		self.s.addDefaultHandlers()
		self.s.addMsgHandler("/print", self.printing_handler)
		self.s.addMsgHandler("/sys/port", self.sys_port_handler)
		self.s.addMsgHandler("/led", self.led_handler)
		self.st = threading.Thread(target=self.s.serve_forever)
		self.st.start()
		print "Starting OSCServer."
		
		while self.alive is True:
			time.sleep(1)
			
		print "time to stop"
		self.st.join()
		
		print "joined??"
		
	def close(self):
		self.alive = False
		
				

def identify():
	""" search string in /dev to identify device associated with this class"""
	return ("m64", MonomeSeries)


if __name__ == "__main__":
	c = MonomeSeries()

	try:
		while True:
			pass
	except KeyboardInterrupt:
		c.close()