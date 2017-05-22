"""
Ethan P. Gould
ethanpgould@gmail.com

File contains function find_k_nearest_neighbors().
Returns the nearest data points to a given numpy vector. 
Output is a k x (n+1) matrix. 

"""
import numpy as np 
from euclidean_distance import euclidean_distance
from create_data import create_data
from integerize_labels import integerize_labels
from split import split

def find_k_nearest_neighbors(test_point, train_data, k):

	distances = []
	for row in train_data:
		distance = euclidean_distance(test_point, row)
		distances.append(distance)
	# ordered list of float value distances 
	distances.sort()
	k_nearest_distances = distances[:k]

	k_nearest_neighbors = np.empty((1,5), dtype= object)

	for row in train_data:
		if euclidean_distance(row, test_point) in k_nearest_distances:
			k_nearest_neighbors = np.append(k_nearest_neighbors,[row],axis=0)

	k_nearest_neighbors = np.delete(k_nearest_neighbors, 0, 0)
	return k_nearest_neighbors

#### Internal Testing ####
if __name__ == '__main__':

	split_data = split(integerize_labels(create_data('iris.txt'))[0])

	train_data = split_data[0]
	test_point = split_data[1][0]

	print("Nearest Neightbors:\n", find_k_nearest_neighbors(test_point, train_data, 10))
