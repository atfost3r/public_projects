#! python3

# main.py - This is the main part of the program for fitness universe updating and computing

from datetime import date
import bodyCalc

#Get the current date

today = date.today()
#set the date format to m/d/y
dt_string = today.strftime("%m/%d/%y")

#Get user inputs for the day
print("Updating Fitness log for: ", dt_string)
print("/n")
weight = float(input("Weight:"))
calories_actual = float(input("Calories:"))
protein_actual = float(input("Protein:"))
carbs_actual = float(input("Carbs:"))
fat_actual = float(input("Fat:"))

#Check if the user wants to update measurements
answer = input("Want to update your measurements? \n y/n? \n")
if answer == "y":
    bicep_r = input("Right Bicep:")
    bicep_l = input("Left Bicep:")
    forearm_r = input("Right Forearm:")
    forearm_l = input("Left Forearm:")
    calf_r = input("Right Calf:")
    calf_l = input("Left Calf:")
    thigh_r = input("Right Thigh:")
    thigh_l = input("Left Thigh:")
    neck = float(input("Neck:"))
    shoulders = input("Shoulders:")
    chest = input("Chest:")
    waist = float(input("Waist:"))
    navy_bodyfat = bodyCalc.bodyFat(waist, neck)

print("Your body fat \%\ is: %.2f", navy_bodyfat)

print("Double checking that it worked: ", weight, calories_actual)