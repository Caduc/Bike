import bike2


#??? Is it possible to define Items in the store.  below is my attempt
#Item2 = bike2.BikeShop ("Item2", bike2.Anns_Med_Model, 2)

print "- - - - - - -"
print ""
print "Welcome to the Breaking Away Bike Shop"
print ""

print "{:^15}{:^15}{:^15}" .format("Item Number", "Item Name", "Quantity")
#??? would it be possible to run through these prints using some sort of count through 6?
print "{:^15}{:^15}{:^+15.0f}" .format(bike2.Item1.itemnumber, bike2.Item1.name, bike2.Item1.Quantity)
print "{:^15}{:^15}{:^+15.0f}" .format(bike2.Item2.itemnumber, bike2.Item2.name, bike2.Item2.Quantity)
print "{:^15}{:^15}{:^+15.0f}" .format(bike2.Item3.itemnumber, bike2.Item3.name, bike2.Item3.Quantity)
print "{:^15}{:^15}{:^+15.0f}" .format(bike2.Item4.itemnumber, bike2.Item4.name, bike2.Item4.Quantity)
print "{:^15}{:^15}{:^+15.0f}" .format(bike2.Item5.itemnumber, bike2.Item5.name, bike2.Item5.Quantity)
print "{:^15}{:^15}{:^+15.0f}" .format(bike2.Item6.itemnumber, bike2.Item6.name, bike2.Item6.Quantity)
print ""
print "-------------"

def Sellthreebikes():
	pass
