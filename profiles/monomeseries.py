import sys, time, random, threading

class MonomeSeries:
	"launch/maintain monome devices"
	
	def __init__(self, name):
		self.name = name
		self.st = threading.Thread(target=self.main)
		self.st.start()
		
	def main(self):
		i = 10
		while i > 1:
			i = i-1
			print "%s: %d" % (self.name, i)
			time.sleep(random.random())
		print self.name + " done"
		

def identify():
	return ("m64", MonomeSeries)
