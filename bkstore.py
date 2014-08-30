import bike2
print "- - - - - - -"
print ""
print "Welcome to the Breaking Away Bike Shop"
print ""

print "Bikes from Bob's Shop.  Weight is given in pounds"
print "Name  :{} {} {}" .format(bike2.Bobs_Cheap_Model.name, bike2.Bobs_Mid_Model.name, bike2.Bobs_Exp_Model.name)
print "Weight:{:^15d}{:^15d}{:^15d}" .format(bike2.Bobs_Cheap_Model.weight, bike2.Bobs_Mid_Model.weight, bike2.Bobs_Exp_Model.weight)
print ""
#print bike2.Ann.made_by()
print "Bikes from Annies Shop.  Weight is given in pounds"
print "Name  :{:^15}{:^15}{:^15}" .format(bike2.Anns_Cheap_Model.name, bike2.Anns_Mid_Model.name, bike2.Anns_Exp_Model.name)
print "Weight:{:^15d}{:^15d}{:^15d}" .format(bike2.Anns_Cheap_Model.weight, bike2.Anns_Mid_Model.weight, bike2.Anns_Exp_Model.weight)
print ""
print "-------------"
