#bike 2
class BobsBikeFactory(object):
    """docstring for BobsBikeFactory"""
    def __init__(self, name):
        self.name = name

    def made_by(self):
        print "%s made this" % (self.name)


class BobWheel(BobsBikeFactory):
    """docstring for Wheel"""
    def __init__(self, style, wheel_weight, wheel_cost):
        self.style = style
        self.wheel_weight = wheel_weight
        self.wheel_cost = wheel_cost

    def cost(self):
        print "the cost of the %s is %s" % (self.style, self.wheel_cost) 


class BobFrame(BobsBikeFactory):
    """docstring for BobFrame"""
    def __init__(self, type, frame_weight, framecost):
        self.type = type
        self.frame_weight = frame_weight
        self.framecost = framecost


# tabling this idea for a bit
class BikebyBob(BobsBikeFactory):
    """docstring for BikebyBob"""
    def __init__(self, name, wheel, frame):
        self.name = name
        self.weight = (wheel.wheel_weight * 2) + (frame.frame_weight)
        self.cost = (wheel.wheel_cost * 2) + (frame.frame_cost)
        # self.wheel = wheel
        # self.frame = frame

    # def get_weight(self):
    #     total_weight = (self.wheel.wheel_weight * 2) + (frame.frame_weight)
    #     return total_weight


bob_mag_wheel = BobWheel("Mag Wheel", 32, 30)
bob_spoke_wheel = BobWheel("Spoke Wheel", 22, 50)
bob_solid_wheel = BobWheel("Solid Wheel", 12, 70)


bob_alum_frame = BobFrame("Aluminum Frame", 44, 400)
bob_carbon_frame = BobFrame("Carbon Frame", 24, 700)
bob_steel_frame = BobFrame("Steel Frame", 64, 100)	


def total_frame_weight(frames):
    """
    Returns the total weight of all frames.
    frames should be a list of BobFrame
    e.g. total_frame_weight([bob_alum_frame, bob_carbon_frame, bob_steel_frame])
    """
    total_weight = 0
    for frame in frames:
        total_weight = total_weight + frame.frameweight 
    return total_weight


def total_weight(things):
    total_weight = 0
    for thing in things:
        total_weight = total_weight + thing.weight 
    return total_weight


Bob = BobsBikeFactory("Bobby")

some_bike = BikebyBob("Cheap Bike", bob_mag_wheel, bob_steel_frame)

if __name__ == "__main__":
    Bob.made_by()
    bob_mag_wheel.cost()

    print "Name: %s" % some_bike.name
    print "Weight: %i" % some_bike.weight
    print "Cost: %i" % some_bike.cost
