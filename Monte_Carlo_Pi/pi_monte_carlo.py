#!/usr/bin/env python		
#Added shebang to make script executable

# Monte Carlo Pi Calculation 
# by Brad Snios
# 5/16/15  
# Compiled to run on python 2.6

from __future__ import division	#Needed since division in python prior to 3.0 is stupid
import random			#Used for random number creation
import time			#Used to calculate run time for program

N_POINTS = 10**8 		#Number of iterations

def pi_calculation(n): 
	return 4. * sum(1 for _ in xrange(0,n,1) if (random.random()**2+random.random()**2) < 1) /n
	#Returns pi as calculated by summing all points within a circle of radius 1 
	#and dividing it by the total number of iterations.
	#Note: the result is multiplied by 4 as these calculations are only
	#performed for one quadrant of the circle


if __name__ == "__main__": 
#Ensures the program is being run directly
	start = time.clock()
	#Initializes run time clock 	

	x = pi_calculation(N_POINTS)
	#Excutes pi_calculation module and print results

	end = time.clock()
	#Ends run time clock 

	file = open('%.0e' % N_POINTS  + "_output.dat","w")
	file.write("Number of runs: " + '%.0e' % N_POINTS + "\n")
	file.write("Pi: " + str(x) + "\n") 
	file.write("Total time: " + str(end-start) + " seconds \n")
	file.close()
	#Creates output file and prints out value of pi and time of calculation

#################
#Version
#1.0 - Initial build of code
#1.1 - Added import division text to force float variable from division.
#      This is needed for all versions of python pre-3.0
#    - Added additional comments to program
#1.2 - Added output of data to a file 
#1.3 - Added shebang line to make the script executable
#1.4 - Replaced range with xrange to remove memory overflow at higher iterations
