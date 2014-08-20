class Made_by_Bob(object):
	"""docstring for Made_by_Bob"""
	def __init__(self, name):
		self.name = name

	def Made_By(self):
		print "I'm made by: %s" % (self.name)
		
class BobWheel(Made_by_Bob):
	"""docstring for Wheel"""
	def __init__(self, style, wheelweight, wheelcost):
		self.style = style
		self.wheelweight = wheelweight
		self.wheelcost = wheelcost

class BobFrame(Made_by_Bob):
	"""docstring for BobFrame"""
	def __init__(self, type, frameweight, framecost):
		self.type = type
		self.frameweight = frameweight
		self.framecost = framecost
		

Bob_mag_wheel = BobWheel("Mag Wheel", 32, 30)
Bob_spoke_wheel = BobWheel("Spoke Wheel", 22, 50)
Bob_solid_wheel = BobWheel("Solid Wheel", 12, 70)


Bob_Alum_frame = BobWheel("Aluminum Frame", 44, 400)
Bob_Carbon_frame = BobWheel("Carbon Frame", 24, 700)
Bob_Steel_frame = BobWheel("Steel Frame", 64, 100)

Bob_mag_wheel.Made_By()

def expensive_bob(wheelcost, framecost):
	pass
		