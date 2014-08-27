#
#  Bob's bike factory definition
#
class BobsBikeFactory(object):
    """docstring for BobsBikeFactory"""
    def __init__(self, name):
        self.name = name

    def cost(self):
        print "the cost of the %s is %s" % (self.style, self.wheel_cost) 

    def made_by(self):
        print "  "
        print "---- This was proudly made by {} at their factory" .format(self.name)

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
    def __init__(self, type, frame_weight, frame_cost):
        self.type = type
        self.frame_weight = frame_weight
        self.frame_cost = frame_cost

class BobsBikeModel(BobsBikeFactory):
    """docstring for BobsBikeModel"""
    def __init__(self, name, wheel, frame):    
        self.name = name
        self.weight = (wheel.wheel_weight * 2) + (frame.frame_weight)
        self.cost = (wheel.wheel_cost * 2) + (frame.frame_cost)
        self.sell = round(((wheel.wheel_cost * 2) + (frame.frame_cost)) * 1.3)
        self.shopsell = round((((wheel.wheel_cost * 2) + (frame.frame_cost)) * 1.3) * 1.2)

#
#  Ann's bike factory definition
#

class AnnsBikeFactory(object):
    """docstring for AnnsBikeFactory"""
    def __init__(self, name):
        self.name = name

    def made_by(self):
        print "  "
        print "---- This was proudly made by {} at their factory" .format(self.name)


class AnnWheel(AnnsBikeFactory):
    """docstring for Wheel"""
    def __init__(self, style, wheel_weight, wheel_cost):
        self.style = style
        self.wheel_weight = wheel_weight
        self.wheel_cost = wheel_cost

    def cost(self):
        print "the cost of the %s is %s" % (self.style, self.wheel_cost) 


class AnnFrame(AnnsBikeFactory):
    """docstring for AnnFrame"""
    def __init__(self, type, frame_weight, frame_cost):
        self.type = type
        self.frame_weight = frame_weight
        self.frame_cost = frame_cost

class AnnsBikeModel(AnnsBikeFactory):
    """docstring for AnnsBikeModel"""
    def __init__(self, name, wheel, frame):    
        self.name = name
        self.weight = (wheel.wheel_weight * 2) + (frame.frame_weight)
        self.cost = (wheel.wheel_cost * 2) + (frame.frame_cost)
        #self.sell = round(((wheel.wheel_cost * 2) + (frame.frame_cost)) * 1.6)
        self.sell = round(self.cost * 1.6)
        self.shopsell = round(self.sell * 1.2)

class Customer(object):
    """docstring for Customer"""
    def __init__(self, customer_name, budget):
        self.customer_name = customer_name
        self.budget = budget

'''
class WrightBrothersShip(object):
    """docstring for WrightBrothersShip"""
    def __init__(self, modelname, quantity):
        self.name = modelname.
        self.bikename = 
 '''       


#
#  Making bob's bikes
#
bob_mag_wheel = BobWheel("Mag Wheel", 32, 30)
bob_spoke_wheel = BobWheel("Spoke Wheel", 23, 40)
bob_solid_wheel = BobWheel("Solid Wheel", 12, 70)

bob_alum_frame = BobFrame("Aluminum Frame", 44, 180)
bob_carbon_frame = BobFrame("Carbon Frame", 24, 400)
bob_steel_frame = BobFrame("Steel Frame", 64, 60)	

Bob = BobsBikeFactory("Bobby")

Bobs_Cheap_Model = BobsBikeModel("Cheapy Bike", bob_mag_wheel, bob_steel_frame)
Bobs_Mid_Model   = BobsBikeModel(" Middy Bike", bob_spoke_wheel, bob_alum_frame)
Bobs_Exp_Model   = BobsBikeModel("Costly Bike", bob_solid_wheel, bob_carbon_frame)

#
#  Making Ann's bikes
#
Ann_mag_wheel = AnnWheel("Mag Wheel", 30, 33)
Ann_spoke_wheel = AnnWheel("Spoke Wheel", 24, 40)
Ann_solid_wheel = AnnWheel("Solid Wheel", 10, 80)

Ann_alum_frame = AnnFrame("Aluminum Frame", 42, 120)
Ann_carbon_frame = AnnFrame("Carbon Frame", 19, 500)
Ann_steel_frame = AnnFrame("Steel Frame", 64, 80)  

Ann = AnnsBikeFactory("Annie")

Anns_Cheap_Model = AnnsBikeModel("Cheapy Bike", Ann_mag_wheel, Ann_steel_frame)
Anns_Mid_Model   = AnnsBikeModel(" Middy Bike", Ann_spoke_wheel, Ann_alum_frame)
Anns_Exp_Model   = AnnsBikeModel("Costly Bike", Ann_solid_wheel, Ann_carbon_frame)

#
#Defining Customers
#
Bart = Customer("Bart", 200)
Mike = Customer("Mike", 500)
Angie = Customer("Angie", 1000)


def AffordableBikes():
    pass

if __name__ == "__main__":
    Bob.made_by()

    print "Name  :{:^15}{:^15}{:^15}" .format(Bobs_Cheap_Model.name, Bobs_Mid_Model.name, Bobs_Exp_Model.name)
    print "Weight:{:^15d}{:^15d}{:^15d}" .format(Bobs_Cheap_Model.weight, Bobs_Mid_Model.weight, Bobs_Exp_Model.weight)
    print "Cost  :{:^15d}{:^15d}{:^15d}"      .format(Bobs_Cheap_Model.cost, Bobs_Mid_Model.cost, Bobs_Exp_Model.cost)
    print "Upcost:{:^15.0f}{:^15.0f}{:^15.0f}".format(Bobs_Cheap_Model.sell, Bobs_Mid_Model.sell, Bobs_Exp_Model.sell)
    print "Shop $:{:^15.0f}{:^15.0f}{:^15.0f}".format(Bobs_Cheap_Model.shopsell, Bobs_Mid_Model.shopsell, Bobs_Exp_Model.shopsell)
    Ann.made_by()

    print "Name  :{:^15}{:^15}{:^15}" .format(Anns_Cheap_Model.name, Anns_Mid_Model.name, Anns_Exp_Model.name)
    print "Weight:{:^15d}{:^15d}{:^15d}" .format(Anns_Cheap_Model.weight, Anns_Mid_Model.weight, Anns_Exp_Model.weight)
    print "Cost  :{:^15d}{:^15d}{:^15d}" .format(Anns_Cheap_Model.cost, Anns_Mid_Model.cost, Anns_Exp_Model.cost)
    print "Upcost:{:^15.0f}{:^15.0f}{:^15.0f}".format(Anns_Cheap_Model.sell, Anns_Mid_Model.sell, Anns_Exp_Model.sell)
    print "Shop $:{:^15.0f}{:^15.0f}{:^15.0f}".format(Anns_Cheap_Model.shopsell, Anns_Mid_Model.shopsell, Anns_Exp_Model.shopsell)
    print " - - - - - - "
    print " "

     
