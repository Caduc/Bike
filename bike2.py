#
#  General Bike factory definition
#

class BikeFactory(object):
    """docstring for BikeFactory"""
    def __init__(self, name):
        self.name = name

    def made_by(self):
        print "  "
        print "---- This was proudly made by {} at their factory" .format(self.name)


class Wheel(BikeFactory):
    """docstring for Wheel"""
    def __init__(self, style, wheel_weight, wheel_cost):
        self.style = style
        self.wheel_weight = wheel_weight
        self.wheel_cost = wheel_cost

    def cost(self):
        print "the cost of the %s is %s" % (self.style, self.wheel_cost) 


class Frame(BikeFactory):
    """docstring for Frame"""
    def __init__(self, type, frame_weight, frame_cost):
        self.type = type
        self.frame_weight = frame_weight
        self.frame_cost = frame_cost

class BikeModel(BikeFactory):
    """docstring for BikeModel"""
    def __init__(self, name, wheel, frame):    
        self.name = name
        self.weight = (wheel.wheel_weight * 2) + (frame.frame_weight)
        self.cost = (wheel.wheel_cost * 2) + (frame.frame_cost)
        self.sell = round(self.cost * 1.6)
        self.shopsell = round(self.sell * 1.2)

class Customer(object):
    """docstring for Customer"""
    def __init__(self, customer_name, budget):
        self.customer_name = customer_name
        self.budget = budget

    def canafford(self, shopsell):
        # If budget > than shopsell print yes
        if self.budget > shopsell: 
            return "yes"
        else:
            return "no"

    def purchdiff(self, shopsell):
        return self.budget - shopsell


#
#  Making bob's bikes
#
bob_mag_wheel = Wheel("Mag Wheel", 32, 15)
bob_spoke_wheel = Wheel("Spoke Wheel", 23, 40)
bob_solid_wheel = Wheel("Solid Wheel", 12, 50)

bob_alum_frame = Frame("Aluminum Frame", 44, 185)
bob_carbon_frame = Frame("Carbon Frame", 24, 300)
bob_steel_frame = Frame("Steel Frame", 64, 60)	

Bob = BikeFactory("Bobby")

Bobs_Cheap_Model = BikeModel("Cheapy Bike", bob_mag_wheel, bob_steel_frame)
Bobs_Mid_Model   = BikeModel(" Middy Bike", bob_spoke_wheel, bob_alum_frame)
Bobs_Exp_Model   = BikeModel("Costly Bike", bob_solid_wheel, bob_carbon_frame)

#
#  Making Ann's bikes
#
Ann_mag_wheel = Wheel("Mag Wheel", 30, 33)
Ann_spoke_wheel = Wheel("Spoke Wheel", 24, 40)
Ann_solid_wheel = Wheel("Solid Wheel", 10, 60)

Ann_alum_frame = Frame("Aluminum Frame", 42, 120)
Ann_carbon_frame = Frame("Carbon Frame", 19, 400)
Ann_steel_frame = Frame("Steel Frame", 64, 80)  

Ann = BikeFactory("Annie")

Anns_Cheap_Model = BikeModel("Cheapy Bike", Ann_mag_wheel, Ann_steel_frame)
Anns_Mid_Model   = BikeModel(" Middy Bike", Ann_spoke_wheel, Ann_alum_frame)
Anns_Exp_Model   = BikeModel("Costly Bike", Ann_solid_wheel, Ann_carbon_frame)

#
#Defining Customers
#
Bart = Customer("Bart", 200)
Mike = Customer("Mike", 500)
Angie = Customer("Angie", 1000)


#def AffordableBikes():
    # yes or no if the cost of the bike is less than the budget.
    

if __name__ == "__main__":
    Bob.made_by()

    print "{:>17}{:^15}{:^15}{:^15}" .format("Name:",Bobs_Cheap_Model.name, Bobs_Mid_Model.name, Bobs_Exp_Model.name)
    print "{:>17}{:^15d}{:^15d}{:^15d}" .format("Weight:",Bobs_Cheap_Model.weight, Bobs_Mid_Model.weight, Bobs_Exp_Model.weight)
    print "{:>17}{:^15d}{:^15d}{:^15d}" .format("Cost:",Bobs_Cheap_Model.cost, Bobs_Mid_Model.cost, Bobs_Exp_Model.cost)
    print "{:>17}{:^15.0f}{:^15.0f}{:^15.0f}".format("Upcost:",Bobs_Cheap_Model.sell, Bobs_Mid_Model.sell, Bobs_Exp_Model.sell)
    print "{:>17}{:^15.0f}{:^15.0f}{:^15.0f}".format("Shop Cost:",Bobs_Cheap_Model.shopsell, Bobs_Mid_Model.shopsell, Bobs_Exp_Model.shopsell)
    print "{:>17}{:^15}{:^15}{:^15}".format("Bart Purch:",Bart.canafford(Bobs_Cheap_Model.shopsell), Bart.canafford(Bobs_Mid_Model.shopsell), Bart.canafford(Bobs_Exp_Model.shopsell))
    print "{:>17}{:^15}{:^15}{:^15}".format("Mike Purch:",Mike.canafford(Bobs_Cheap_Model.shopsell), Mike.canafford(Bobs_Mid_Model.shopsell), Mike.canafford(Bobs_Exp_Model.shopsell))
    print "{:>17}{:^15}{:^15}{:^15}".format("Angie Purch:",Angie.canafford(Bobs_Cheap_Model.shopsell), Angie.canafford(Bobs_Mid_Model.shopsell), Angie.canafford(Bobs_Exp_Model.shopsell))
    Ann.made_by()

    print "{:>17}{:^15}{:^15}{:^15}" .format("Name:",Anns_Cheap_Model.name, Anns_Mid_Model.name, Anns_Exp_Model.name)
    print "{:>17}{:^15d}{:^15d}{:^15d}" .format("Weight:",Anns_Cheap_Model.weight, Anns_Mid_Model.weight, Anns_Exp_Model.weight)
    print "{:>17}{:^15d}{:^15d}{:^15d}" .format("Cost:",Anns_Cheap_Model.cost, Anns_Mid_Model.cost, Anns_Exp_Model.cost)
    print "{:>17}{:^15.0f}{:^15.0f}{:^15.0f}".format("Upcost:",Anns_Cheap_Model.sell, Anns_Mid_Model.sell, Anns_Exp_Model.sell)
    print "{:>17}{:^15.0f}{:^15.0f}{:^15.0f}".format("Shop Cost:",Anns_Cheap_Model.shopsell, Anns_Mid_Model.shopsell, Anns_Exp_Model.shopsell)
    print "{:>17}{:^15}{:^15}{:^15}".format("Bart Purch:",Bart.canafford(Anns_Cheap_Model.shopsell), Bart.canafford(Anns_Mid_Model.shopsell), Bart.canafford(Anns_Exp_Model.shopsell))
    print "{:>17}{:^15}{:^15}{:^15}".format("Mike Purch:",Mike.canafford(Anns_Cheap_Model.shopsell), Mike.canafford(Anns_Mid_Model.shopsell), Mike.canafford(Anns_Exp_Model.shopsell))
    print "{:>17}{:^15}{:^15}{:^15}".format("Angie Purch:",Angie.canafford(Anns_Cheap_Model.shopsell), Angie.canafford(Anns_Mid_Model.shopsell), Angie.canafford(Anns_Exp_Model.shopsell))    
#    print "{:>17}{:^+15.0f}{:^+15.0f}{:^+15.0f}".format("Angie Diff:", Angie.purchdiff(Anns_Cheap_Model.shopsell),Angie.purchdiff(Anns_Mid_Model.shopsell), Angie.purchdiff(Anns_Exp_Model.shopsell))
    print " - - - - - - "
    print " "

     
