#################
#
#
# 
###################

import time
import sys

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

#takes in the weight of the coin jar as a reference
currentJar = hx.get_weight(5)
#open file
f= open("Coins.txt", 'r')
#initialize the list
Coins = []
#read each line and add it to the list
fl = f.readlines()
for x in fl:
	Coins.append(int(x))
#closes file to preserve memory
f.close()

#moves data to local variables
pennies = Coins[0]
nickels = Coins[1]
dimes = Coins[2]
quarters = Coins[3]

while True:
    try:
        #starts the loop by checking the new weight relative to the initial
        newJar = hx.get_weight(5)
        if (newJar > currentJar):
			#pause for a second to let the coin setle
			time.sleep(1)
			# if chenge in weight, calculated the weight of the new addition (the new coin)
			coinWeight = newJar-currentJar
		
			#checks the coinWeight against the weights of each coin type to determine its type
			#checks in a range of .1 grams away from the expected weight of the coin for expected error
			if ((coinWeight >= 2.4) and (coinWeight <= 2.6)):
				pennies += 1
				currentJar = hx.get_weight(5)
				break
				print "{} is a penny".format(coinWeight)
			elif ((coinWeight >= 4.9) and (coinWeight <= 5.1)):
				nickels += 1
				currentJar = hx.get_weight(5)
				print "{} is a nickel".format(coinWeight)
				break
			elif ((coinWeight >= 2.168) and (coinWeight <= 2.368)):
				dimes += 1
				currentJar = hx.get_weight(5)
				print "{} is a dime".format(coinWeight)
				break
			elif ((coinWeight >= 11.24) and (coinWeight <= 11.44)):
				quarters += 1
				currentJar = hx.get_weight(5)
				print "{} is a quarter".format(coinWeight)
				break
			elif (coinWeight < 2.167):
				#the weight wasnt a coin but some small change, so it should ignore it and go back to the loop
				pass
			elif (coinWeight > 11.45):
				#too large and should produce an error message
				print "Could not identify coin, please remove and try placing the coins in one at a time."
				while (newJar > currentJar):
					time.sleep(1)
					print "waiting"
					
			#writes down the # of each coin in external file
			f = open("Coins.txt", 'w')
			f.write("{}\n{}\n{}\n{}".format(pennies, nickels, dimes, quarters))

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()

	#write the # of coins to a external text file if format
	#penny
	#nickel
	#dime
	#quarter