#Nick True
#26/9/2014

name1 = "nick"
print name1, "worked on this lab"
print
name1 = raw_input("What is your Name?" +"\n")
favRestaurant1 = raw_input("What is your favriot resteraunt, " +name1 +"?" +"\n")
print name1, "likes" , favRestaurant1 , "the best!"
mealCost = raw_input("How expensive was your meal?" +"\n")
mealCost = float(mealCost)
tax = 0.06*mealCost
tipRate = raw_input('How much do you want to tip (%)?')
tipRate = float(tipRate)
tip2 = tipRate/100
tip3 = tip2*mealCost
final = mealCost+tax+tip3
print name1 , "spent" , final , "eating at" , favRestaurant1
