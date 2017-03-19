"""
Ethan P. Gould, epg2133
Engineering 1006, HW5 

File contains function integerize_labels. 
	Loops over input matrix rows creating dictionary that correleates str 
	labels with a unique integer {0,1,...} for each. 

	Input: Matrix of data will final column of str label names
	Output: Matrix of identical dimentions, with strs replaces with ints 
"""
import numpy as np
from create_data import create_data

def integerize_labels(data):

	label_dict = {}
	integerized_data = np
	labels_counter = 0 
	
	for row in data:
		# look at the last column entry in each row
		if row[-1] not in label_dict.keys():
			# add that shit and change 
			label_dict[row[-1]] = labels_counter
			row[-1] = labels_counter
			# increment the label counter 
			labels_counter += 1

		else:
			# change the value to what's associated in the dictionary 
			digit_label = label_dict[row[-1]]
			row[-1] = digit_label

	integerized_data = data
	return (integerized_data, label_dict)