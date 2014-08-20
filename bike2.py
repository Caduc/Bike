#bike 2
class BobMadeThis(object):
	"""docstring for BobMadeThis"""
	def __init__(self, name):
		self.name = name

	def Madeby(self):
		print "%s made this" % (self.name)

class BobWheel(BobMadeThis):
	"""docstring for Wheel"""
	def __init__(self, style, wheelweight, wheelcost):
		self.style = style
		self.wheelweight = wheelweight
		self.wheelcost = wheelcost

	def wcost(self):
		print "the cost of the %s is %s" % (self.style, self.wheelcost) 

class BobFrame(BobMadeThis):
	"""docstring for BobFrame"""
	def __init__(self, type, frameweight, framecost):
		self.type = type
		self.frameweight = frameweight
		self.framecost = framecost
'''
tabling this idea for a bit
class BikebyBob(BobMadeThis):
	"""docstring for BikebyBob"""
	def __init__(self, bobbike,):
		self.arg = arg

'''		

def Costbobbike(wheelcost,):
	pass

Bob_mag_wheel = BobWheel("Mag Wheel", 32, 30)
Bob_spoke_wheel = BobWheel("Spoke Wheel", 22, 50)
Bob_solid_wheel = BobWheel("Solid Wheel", 12, 70)


Bob_Alum_frame = BobWheel("Aluminum Frame", 44, 400)
Bob_Carbon_frame = BobWheel("Carbon Frame", 24, 700)
Bob_Steel_frame = BobWheel("Steel Frame", 64, 100)	

Bob = BobMadeThis("Bobby")

Bob.Madeby()
Bob_mag_wheel.wcost()