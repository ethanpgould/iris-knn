"""
Ethan P. Gould, epg2133
Engineering 1006, HW5 

File contains function comparing the predicted labels of the test set to the 
labels found in the final column of the test data matrix. Returns a float 
value for error percentage. 
"""
import numpy as np 

def calculate_error_rate(predicted_labels, test_data):

	num_errors = 0 
	for i in range(test_data.shape[0]):
		if predicted_labels[i,0] != test_data[i,-1]:
			num_errors += 1

	error_rate = num_errors / test_data.shape[0]

	return error_rate