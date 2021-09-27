#!python3

#dietCalc.py - this subroutine will take current body stats and and calculate the calories, protein, carbs and fat that should be the goal



def harris_benedict(weight, height, age):
    BMR = 66+(6.2*weight)+(12.7*height)-(6.76*age)
    return BMR

