"""
Ethan P. Gould, epg2133
Engineering 1006, HW5 

File implements the utility of different knn components. 
"""

import numpy as np
from find_k_nearest_neighbors import find_k_nearest_neighbors
from majority_vote import majority_vote

def knn(train_data, test_data, k):

	predicted_labels = np.empty((1,1), dtype= int)
	for row in test_data:

		row_neighbors = find_k_nearest_neighbors(row, train_data, k)

		pd_label = majority_vote(row_neighbors)

		predicted_labels = np.append(predicted_labels, \
			np.array(pd_label).reshape((1,1)), axis= 0)

	# remove initialization row 
	predicted_labels = np.delete(predicted_labels,0,0)
	return predicted_labels

# Internal Testing 
# integerized_data = integerize_labels(create_data('iris.txt'))[0]
# train, test = split(integerized_data)