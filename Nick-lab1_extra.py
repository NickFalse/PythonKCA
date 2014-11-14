act = raw_input("what activity shall i run? ")
act = int(act)
print 'running activity' , act
print "\n"
###Activity 1
if act == 1:
    week = long(24*7)
    day = long((24*60)*60)
    mon6 = long((day*30)*6)
    year = long((week*60)*78)
    print "there are" , week , "hours in a week, " , day , "seconds in a day, " , mon6 , "seconds in six months and " , year , "minutes in 1.5 years."
    raw_input ("")
###Activity 2
elif act == 2:
    import math
    print "Area of a circle"
    rad = float(raw_input("radius:" +"\n"))
    radius = rad*rad
    radius = float(radius)
    total = float(math.pi * radius)
    print "area =" , total
    raw_input ("")
###Activity 3
elif act == 3:
    print "there" +"\'" +"s a snake in my boots"
    raw_input ("")
###Activity 4
elif act == 4:
    my_string = "actdgo"
    print my_string[1] +my_string[0] +my_string[2] , my_string[3] +my_string[5] +my_string[4]
    raw_input ("")
else:
    print "maybe later"
    raw_input("")
    
