#! python3

# main.py - This is the main part of the program for fitness universe updating and computing

from datetime import date
import bodyCalc, automation, progress


# Get the current date

today = date.today()
dayOfTheWeek = date.today().weekday()  # Get the current day of the week
# set the date format to m/d/y
dt_string = today.strftime("%m/%d/%y")

# Alex's Birthday
birthday = date(1991, 10, 9)
# Calculate age
age = (
    today.year
    - birthday.year
    - ((today.month, today.day) < (birthday.month, birthday.day))
)

# automatic update logic

## Run daily updates
weight = automation.dailyUpdate(dt_string)
# Calulate progress
progress.progressDaily()

# Weekly update
if dayOfTheWeek == 5:  # Update some stuff on Saturdays
    (
        bicep_l,
        bicep_r,
        forearm_l,
        forearm_r,
        calf_l,
        calf_r,
        thigh_l,
        thigh_r,
        shoulders,
        chest,
        waist,
        navy_bodyfat,
    ) = automation.weeklyUpdate(dayOfTheWeek)
    leanWeight, fatWeight = bodyCalc.bodyComp(weight, navy_bodyfat)
    print("Your body fat percentage is: {:2.2f}% ".format(navy_bodyfat * 100))
    print(
        "You you have {:3.2f}  pounds of fat and {:3.2f} pounds of lean mucsle".format(
            leanWeight, fatWeight
        )
    )
    # Check Macro adherence

    # []TODO: calculate average calorie delta for the week
    # data = import_csv(file_name)
    # last_row = data[-1]

    # [] TODO: Check status of calories, weight, protein, etc.

    # [] TODO: Recalulate calories and macros goal
    #
    #


# [] TODO: Save off necessary variables to be read in next time the program is run
