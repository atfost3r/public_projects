#!python3

# automation.py - this script is used to automate the timing and input types that are being done

import bodyCalc, dietCalc

def dailyUpdate():   # Create function to do the daily update of data


    return

def weeklyUpdate(dayOfTheWeek):
    
    print('Time to Update your body measurements.\nGrab a tape measure!')
    bicep_r = float(input("Right Bicep (in): "))
    bicep_l = float(input("Left Bicep (in): "))
    forearm_r = float(input("Right Forearm (in): "))
    forearm_l = float(input("Left Forearm (in): "))
    calf_r = float(input("Right Calf (in): "))
    calf_l = float(input("Left Calf (in): "))
    thigh_r = float(input("Right Thigh (in): "))
    thigh_l = float(input("Left Thigh (in): "))
    neck = float(input("Neck (in): "))
    shoulders = float(input("Shoulders (in): "))
    chest = float(input("Chest (in): "))
    waist = float(input("Waist (in): "))
    navy_bodyfat = bodyCalc.bodyFat(waist, neck)    #calculate body fat percentage with U.S. Navy's formula
    [goals] = dietCalc()
    return bicep_l,bicep_r,forearm_l,forearm_r,calf_l, calf_r, thigh_l, thigh_r,shoulders,chest,waist,navy_bodyfat