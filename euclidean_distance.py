"""
Ethan P. Gould
ethanpgould@gmail.com

Function takes two numpy vectors of length (n+1) and computes the euclidean 
distance between the first n values of each vector. Returns a float value. 
"""
import numpy as np
import math 

def euclidean_distance(x1,x2):

	# remove the type index from the end
	x1_clipped = x1[:-1]
	x2_clipped = x2[:-1]

	vector_diff = x1_clipped - x2_clipped
	diff_square = vector_diff ** 2 
	distance = math.sqrt(diff_square.cumsum()[-1])

	return distance
