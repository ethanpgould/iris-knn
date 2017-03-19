"""
Ethan P. Gould, epg2133
Engineering 1006, HW5 

File contains funciton split() that parses an input matrix, selecting 15 
random instances of each type for output test_data. The remaining instances 
of each type constitue train_data. 15 is hardcoded, but can be modified. 

Function does not depend on number of columsn in the matrix, number of types 
in the matrix, number of instances per type, or on the order of the types
occurance in the entry matrix. 
"""
import numpy as np
from create_data import create_data
from integerize_labels import integerize_labels

def split(integerized_data):

	# dictionariess of types and number of rows per type in intergerized_data
	rows_dict = {}
	for row in integerized_data:
		if row[-1] not in rows_dict.keys():
			rows_dict[row[-1]] = 1
		else:
			rows_dict[row[-1]] += 1

	# initalize a test_data matrix and train_data matrix
	test_data = np.empty((1,5), dtype= object)
	train_data = np.empty((1,5), dtype= object)

	for i in rows_dict.keys():

		holding_matrix = np.empty((1,5), dtype= object)

		for row in integerized_data:
			if row[-1] == i: 
				row = row.reshape((1,5))
				# add all the rows for a specific i 
				holding_matrix = np.append(holding_matrix, row, axis= 0)
		# remove the None row
		holding_matrix = np.delete(holding_matrix, 0, 0)

		# print("Unshuffled:\n", holding_matrix)
		# print("Length:\n", holding_matrix.shape[0])
		np.random.shuffle(holding_matrix)

		# add the first fifteen to test_data
		test_data = np.append(test_data, holding_matrix[:15], axis= 0)
		# add the rest to train_data
		train_data = np.append(train_data, holding_matrix[15:], axis= 0)

	#remove the None rows from test and train 
	test_data = np.delete(test_data, 0, 0)
	train_data = np.delete(train_data, 0, 0)

	############ Testing ##################
	# print("Testing data:\n", test_data)
	# print("Training data:\n", train_data)

	return(train_data, test_data)
