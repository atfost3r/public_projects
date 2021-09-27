#! python3

# main.py - This is the main part of the program for fitness universe updating and computing

from datetime import date
import bodyCalc, automation

#Get the current date

today = date.today()
dayOfTheWeek = date.today().weekday()   # Get the current day of the week
#set the date format to m/d/y
dt_string = today.strftime("%m/%d/%y")




#automatic update logic

## Run daily updates
#Get user inputs for the day
print("Updating Fitness log for: ", dt_string)

weight = float(input("Weight:"))
calories_actual = float(input("Calories:"))
protein_actual = float(input("Protein:"))
carbs_actual = float(input("Carbs:"))
fat_actual = float(input("Fat:"))

#Weekly update
if dayOfTheWeek == 6: # Update some stuff on Saturdays
    bicep_l,bicep_r,forearm_l,forearm_r,calf_l, calf_r, thigh_l, thigh_r,shoulders,chest,waist,navy_bodyfat = automation.weeklyUpdate(dayOfTheWeek)
    leanWeight, fatWeight = bodyCalc.bodyComp(weight, navy_bodyfat)
    print("Your body fat percentage is: {:2.2f}% ".format(navy_bodyfat*100))
    print("You you have {:3.2f}  pounds of fat and {:3.2f} pounds of lean mucsle".format(leanWeight, fatWeight))




