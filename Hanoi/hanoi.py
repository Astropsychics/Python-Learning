#!/usr/bin/env python

# Tower of Hanoi Solution
# by Brad Snios
# 5/21/15
# Compiled to run on python 2.6

def hanoi(n,tower_start,tower_end,tower_inter,output): 
	if n >= 1: 
		hanoi(n-1,tower_end,tower_start,tower_inter,output)
		output.write("Moving from " + tower_start + " to " + tower_end + "\n")
		hanoi(n-1,tower_inter,tower_end,tower_start,output)
		#Executes recurrsive relation to determine the solution. 
		#Relation function  was dervied from from equation on wikipedia. 	
		#Output is printed to file. 

if __name__ == "__main__": 
#Ensures the program is run directly 

	print("\nWelcome to the Tower of Hanoi solution generator.\n")
	N_DISKS = input("Please input the total number of disks on the tower: ")  
	#Prints greeting and inputs total number of disks	
	
	file_name = str(N_DISKS) + "_disk_solution.dat"
	file = open(file_name,"w")
	file.write("Tower of Hanoi solution for " + str(N_DISKS) + " disks.\n")
	file.write("All disks start on tower 1 and end on tower 2.\n\n")
	#Generates output filename and the file	

	hanoi(N_DISKS,"1","2","3",file)
	file.close()
	#Executes hanoi solution function and prints out solution to file

	file = open(file_name,"a") 	
	num_lines = sum(1 for line in open(file_name)) 
	#Reopens saved file and solves for the total number of lines
	#to find the total number of steps.	
	#Note: there is probably a better way to determine the total number of steps,
	#but it currently eludes me
		
	file.write("\nTotal numbers of steps: " + str(num_lines-3))
	file.close()
	#Outputs steps to complete puzzle to the file

################
#Version
#1.0 - Initial release of code
