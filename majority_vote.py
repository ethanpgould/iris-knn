"""
Ethan P. Gould, epg2133
Engineering 1006, HW5 

Function returns integer representing most frequent type integer.
"""
import numpy as np 

def majority_vote(neighbors):
	# slice off an array of just 
	holding_array = neighbors[:,-1]

	dict = {}
	for item in holding_array:
		if item not in dict.keys():
			dict[item] = 1 
		else:
			dict[item] += 1 

	majority_vote = max(dict, key=dict.get)
	return majority_vote
