#!/usr/bin/env python

# Solar System Model 
# by Brad Snios
# 5/25/15
# Compiled to run on python 2.6

import fractions 	#required for greatest common denominator (gcd) function
import functools 	#required for reduce function
import math 		#required for square root function
import numpy as np	#required to define arrays
import operator		#required for array multiply function

name = np.array(["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"])
#Array of planet names
r = np.array([0.387,0.723,1.000,1.524,5.203,9.523,19.208,30.087])
#Array of planet-Sun radii, in AU 

def least_common_multiple(p): 
	return functools.reduce(operator.mul,p,1) / functools.reduce(fractions.gcd,p)
	#Calculate least common multiple of the various planetary periods to find
	#time until next alignment	

if __name__ == "__main__": 
#Ensures the program is run directly 

	print("\nWelcome to the Solar System Model.")
	print("This model calculates the total number of rotations for each planet")
	print("for a user-set time, as well as the time until next alignment.\n")
	TIME = input("Please input the time elapsed, in Earth years: ")  
	#Greeting and prompts user for TIME input	


	file_name = '%.2e' % TIME  + "_solar_system.dat"
	file = open(file_name,"w")
	file.write("Time: " + str(TIME) + " Earth year(s)\n\n")
	file.close()
	#Generates output file and write out time variable	

	period = [0] * 8	
	#Creates empty list that will be populated with period of each planet in the following loop
	file = open(file_name,"a")
	for i in range(8):
	
		period[i] = math.sqrt( r[i]**3 )
		rotations = TIME / period[i]
		#Calculates period of each planet using Kepler's 3rd Law and determines total number 
		#of rotations. 		

		file.write(name[i] + ": " + '%.5e' % rotations + " rotation(s)\n")
		#Outputs total number of rotations for each planets
	
	alignment = least_common_multiple(period) - TIME 
	file.write("\nTime until next alignment: " + '%.5e' % alignment + " year(s)\n") 
	#Executes LCM function and outputs result	

	file.close()
	#Closes file

################
#Version
#1.0 - Initial release of code
