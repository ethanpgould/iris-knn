"""
Ethan P. Gould
ethanpgould@gmail.com

Function reads and parses.

	input: iris.data imported as a .txt file
	output: numpy matrix of dimensions m, (n+1). First n columns represent 
		features the data set. Final column inclues label for each row. 

"""
import numpy as np 
import csv 

def create_data(input_data_file):

	holding_list = []
	# handle the iris.data as a csv file
	with open(input_data_file, 'r', newline= '') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			if row != []: # do not include empty rows in the data file 
				# every entry except the last needs converstion to type:float
				for i in range(len(row)-1):
					row[i] = float(row[i])

				# add [flt, flt, ... , str] to the holding list
				holding_list.append(row)

	# turn holding list into matrix object containing both flt and str types
	data = np.array(holding_list, dtype= object)
	return data
