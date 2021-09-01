#! python3

# formFiller.py - Automatically fill out the form

import pyautogui, time

# Set the mouse coordinates
nameField = (267, 356)
submitButton = (191, 880)
submitColor = (75, 141, 249)
submitAnotherLink = (303, 229)


formData = [
    {
        "name": "Alice",
        "fear": "eavesdropping",
        "source": "wand",
        "robocop": 4,
        "comments": "tell Bob I sat hi",
    },
    {
        "name": "Bob",
        "fear": "bees",
        "source": "amulet",
        "robocop": 4,
        "comments": "n/a",
    },
    {
        "name": "Carol",
        "fear": "puppets",
        "source": "crystal ball",
        "robocop": 1,
        "comments": "Please take the puppets out of the break room.",
    },
    {
        "name": "Alex Murphy",
        "fear": "ED-209",
        "source": "money",
        "robocop": 5,
        "comments": "Protect the innocent. Serve the public trust. Uphold the law.",
    },
]
pyautogui.PAUSE = 0.5

for person in formData:
    # Give the user a chance to kill the script
    print(">>> 5 SECOND PAUSE TO LET USER PRESS CTL-C <<<")
    time.sleep(5)

    # Wait until the form page has loaded
    while not pyautogui.pixelMatchesColor(
        submitButton[0], submitButton[1], submitColor
    ):
        time.sleep(0.5)
    print("Entering %s info... " % (person["name"]))
    pyautogui.click(nameField[0], nameField[1])

    # Fill out the Name feild
    pyautogui.typewrite(person["name"] + "\t")
    pyautogui.typewrite(person["fear"] + "\t")
