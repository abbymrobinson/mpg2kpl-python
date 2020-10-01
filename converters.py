"""
converters.py
This is a python program to convert MPG to KPL
User is asked to enter a MPG number
number is converted to KPL which is
printed in the command line.
"""
# Declaring known constants
KPM = 1.609344 # kilometers per miles
GPL = .02641720524 # gallons per liter

def mpg2kpl(mpg):
    """
    Converts MPG to KPL via the formula:
    KPL = MPG * KPM * GPL
    """
    return mpg * KPM * GPL

# ask user to input MPG value
mpg = input("What is the MPG?")
# Convert the input into a numeric value
mpg = float(mpg)

#output the converted value rounded to 2 digits
print(round(mpg2kpl(mpg), 2), "kpl")
