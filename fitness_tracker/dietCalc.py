#!python3

# dietCalc.py - this subroutine will take current body stats and and calculate the calories, protein, carbs and fat that should be the goal


def harris_benedict(weight, height, age):
    BMR = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
    return BMR


def bulkMacros(weight):
    # This portion is from 'Bigger Leaner Stronger' by Michael Matthews
    protein = round(weight)  # 1 gram of protein per pound of body
    carbs = 2 * round(weight)  # 2 grams of carbs per pound of body weight
    fat = round(0.4 * weight)
    calories = 4 * (protein + carbs) + (
        9 * fat
    )  # calculate total calories where fat = 9 cals/gram, protein and carbs are 4 cals/gram
    return protein, carbs, fat, calories


def cutMacros(weight, bodyFat):
    # This portion is from 'Bigger Leaner Stronger' by Michael Matthews
    if (
        bodyFat >= 0.25
    ):  # if body fat is higher than 25% then the calculation is slightly different
        protein = round(0.8 * weight)  # 1 gram of protein per pound of body
        carbs = 2 * round(0.6 * weight)  # 2 grams of carbs per pound of body weight
        fat = round(0.3 * weight)

    else:
        protein = round(1.2 * weight)  # 1
        carbs = round(weight)
        fat = round(0.2 * weight)
    calories = 4 * (protein + carbs) + (
        9 * fat
    )  # calculate total calories where fat = 9 cals/gram, protein and carbs are 4 cals/gram
    return protein, carbs, fat, calories


def maintMacros(weight):
    protein = round(1 * weight)  # 1
    carbs = round(1.6 * weight)
    fat = round(0.35 * weight)
    calories = 4 * (protein + carbs) + (
        9 * fat
    )  # calculate total calories where fat = 9 cals/gram, protein and carbs are 4 cals/gram
    return protein, carbs, fat, calories


def refeedMacros(calories, weight):
    protein = round(weight)
    fat = 20  # as little as possible, shoot for <20g of fat
    carbs = (calories - ((4 * protein) + (9 * fat))) / 4
    return protein, carbs, fat


def carbCycling():

    return
