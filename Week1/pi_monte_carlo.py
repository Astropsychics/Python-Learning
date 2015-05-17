# Monte Carlo Pi Calculation 
# by Brad Snios
# 5/16/15 


from __future__ import division	#needed because division in python prior to 3.0 is stupid
import random			#used for random number creation
import time			#used to calculate run time for program

N_POINTS = 10**8 		#Number of iterations

def pi_calculation(n): 
	return 4 * sum(1 for _ in range(n) if (random.random()**2+random.random()**2) < 1) /n
	#returns pi as calculated by summing all points within a circle of radius 1 
	#and dividing it by the total number of iterations.
	#Note: the result is multiplied by 4 as these calculations are only
	#performed for one quadrant of the circle


if __name__ == "__main__": 
#ensures the program is being run directly
	start = time.clock()
	#initializes run time clock 	

	x = pi_calculation(N_POINTS)
	#excutes pi_calculation module and print results

	end = time.clock()
	#ends run time clock 

	file = open("pi_output.dat","w")
	file.write("Pi: " + str(x) + "\n") 
	file.write("Total time: " + str(end-start) + " seconds")
	file.close()
	#creates output file and prints out value of pi and time of calculation

#################
#Version
#1.0 - Initial build of code
#1.1 - Added import division text to force float variable from division.
#      This is needed for all versions of python pre-3.0
#    - Added additional comments to program
#1.2 - Added output of data to a file 
