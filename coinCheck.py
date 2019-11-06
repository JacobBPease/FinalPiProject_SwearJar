#################
#
#
# 
###################

import time
import sys
from Tkinter import *

EMULATE_HX711=True

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711

def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)

# I've found out that, for some reason, the order of the bytes is not always the same between versions of python, numpy and the hx711 itself.
# Still need to figure out why does it change.
# If you're experiencing super random values, change these values to MSB or LSB until to get more stable values.
# There is some code below to debug and log the order of the bits and the bytes.
# The first parameter is the order in which the bytes are used to build the "long" value.
# The second paramter is the order of the bits inside each byte.
# According to the HX711 Datasheet, the second parameter is MSB so you shouldn't need to modify it.
hx.set_reading_format("MSB", "MSB")

# HOW TO CALCULATE THE REFFERENCE UNIT
# To set the reference unit to 1. Put 1kg on your sensor or anything you have and know exactly how much it weights.
# In this case, 92 is 1 gram because, with 1 as a reference unit I got numbers near 0 without any weight
# and I got numbers around 184000 when I added 2kg. So, according to the rule of thirds:
# If 2000 grams is 184000 then 1000 grams is 184000 / 2000 = 92.
#hx.set_reference_unit(113)
hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")

# to use both channels, you'll need to tare them both
#hx.tare_A()
#hx.tare_B()



#add function to calc # of coins of a certain type added
#type determined by #, 0-penny:1-nickel:2-dime:3-quarter
def coinCalc(type, function):

	#takes in the weight of the coin jar as a reference
	currentJar = hx.get_weight(5)
	#open file
	f= open("Coins.txt", 'r')
	#initialize the dictionary
	Values = []
	#read each line and add it to the list
	fl = f.readlines()
	for x in fl:
		Values.append(int(x))
	#transfers values into a coins dictionary for ease of access
	Coins = {}
	Coins['pennies'] = Values[0]
	Coins['nickels'] = Values[1]
	Coins['dimes'] = Values[2]
	Coins['quarters'] = Values[3]
	#closes file to preserve memory
	f.close()

	#"stall" window serves to give the user as much time as they need to add/ remove coins and let them settle

	while True:
		try:
			#starts the loop by checking the new weight relative to the initial
			newJar = hx.get_weight(5)
			if (function):
				#pause for a second to let the coin setle
				time.sleep(1)
				# if chenge in weight, calculated the weight of the new addition (the new coin)
				coinWeight = newJar-currentJar
		
				#checks the coinWeight against the weights of each coin type to determine its type
				#checks in a range of .1 grams away from the expected weight of the coin for expected error
				if (type == 0):
					newPennies = coinWeight / 2.5
					roundedPennies = int(round(newPennies))
					Coins['pennies'] += roundedPennies
				
					writeCoins(pennies, nickels, dimes, quarters)
					break
					
				elif (type == 1):
					newNickels = coinWeight / 5.0
					roundedNickels = int(round(newNickels))
					Coins['nickels'] += roundedNickels
					
					writeCoins(pennies, nickels, dimes, quarters)
					break
					
				elif (type == 2):
					newDimes = coinWeight / 2.268
					roundedDimes = int(round(newDimes))
					int(roundedDimes)
					Coins['dimes'] += roundedDimes
					
					writeCoins(pennies, nickels, dimes, quarters)
					break
					
				else:
					newQuarters = coinWeight / 11.34
					roundedQuarters = int(round(newQuarters))
					int(roundedQuarters)
					Coins['quarters'] += roundedQuarters
					
					writeCoins(pennies, nickels, dimes, quarters)
					break

			else:
				#pause for a second to let the coin setle
				time.sleep(1)
				# if chenge in weight, calculated the weight of the new addition (the new coin)
				coinWeight = currentJar - newJar
		
				#checks the coinWeight against the weights of each coin type to determine its type
				#checks in a range of .1 grams away from the expected weight of the coin for expected error
				if (type == 0):
					newPennies = coinWeight / 2.5
					roundedPennies = int(round(newPennies))
					Coins['pennies'] -= roundedPennies
					
					writeCoins(pennies, nickels, dimes, quarters)
					break
					
				elif (type == 1):
					newNickels = coinWeight / 5.0
					roundedNickels = int(round(newNickels))
					Coins['nickels'] -= roundedNickels
					
					writeCoins(pennies, nickels, dimes, quarters)
					break
					
				elif (type == 2):
					newDimes = coinWeight / 2.268
					roundedDimes = int(round(newDimes))
					Coins['dimes'] -= roundedDimes
					
					writeCoins(pennies, nickels, dimes, quarters)
					break
					
				else:
					newQuarters = coinWeight / 11.34
					roundedQuarters = int(round(newQuarters))
					Coins['quarters'] -= roundedQuarters
					
					writeCoins(pennies, nickels, dimes, quarters)
					break

			hx.power_down()
			hx.power_up()
			time.sleep(0.1)

		except (KeyboardInterrupt, SystemExit):
			cleanAndExit()

#function that writes the new values to the external coins file
def writeCoins(pennies, nickels, dimes, quarters):
	f = open("Coins.txt", 'w')
	f.write("{}\n{}\n{}\n{}".format(Coins['pennies'], Coins['nickels'], Coins['dimes'], Coins['quarters']))
	f.close()

