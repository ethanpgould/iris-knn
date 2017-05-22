"""
Ethan P. Gould
ethanpgould@gmail.com

File contains function to plot the respecitve columns of a matrices containing
flower measurement data using matplotlib. Input matrix is partitions into 
three individual data containers. 
"""
import numpy as np
import matplotlib.pyplot as plt 

######### Internal Testing ##########
# from create_data import create_data
# data = create_data('iris.txt')

def plot_data(data):

	# initialze type specific matrices 
	setosa = np.empty((1,5), dtype= object)
	versicolor = np.empty((1,5), dtype= object)
	virginica = np.empty((1,5), dtype= object)

	# partition data assuming no order or rows 
	for row in data:
		if row[0,-1] == "Iris-setosa":
			setosa = np.append(setosa, row, axis= 0)
		elif row[0,-1] == "Iris-versicolor":
			versicolor = np.append(versicolor, row, axis= 0)
		elif row[0,-1] == "Iris-virginica":
			virginica = np.append(virginica, row, axis= 0)

	# remove the None row 
	setosa = np.delete(setosa, 0, 0)
	versicolor = np.delete(versicolor, 0, 0)
	virginica = np.delete(virginica, 0, 0)

	################################
	# sepal length vs. sepal width #
	################################
	data = {"setosa": [setosa[:,0], setosa[:,1]], 
        	"versicolor": [versicolor[:,0], versicolor[:,1]],
        	"virginica": [virginica[:,0], virginica[:,1]]}

	styles = {"setosa": 'b', 
			"versicolor": 'c',
			"virginica": 'r'}

	fig, ax = plt.subplots()

	for group, data in data.items():
	    ax.plot(data[0], data[1], 'o', color = styles[group], label=group)

	ax.legend()
	plt.title("Sepal Length vs Sepal Width") 
	plt.xlabel('Sepal Length') 
	plt.ylabel('Sepal Width') 
	plt.show()
	plt.savefig("Sepal Length vs Sepal Width")

	##################################
	# septal length vs. petal length # 
	##################################
	data = {"setosa": [setosa[:,0], setosa[:,2]], 
			"versicolor": [versicolor[:,0], versicolor[:,2]],
			"virginica": [virginica[:,0], virginica[:,2]]}

	styles = {"setosa": 'b', 
			"versicolor": 'c',
			"virginica": 'r'}

	fig, ax = plt.subplots()

	for group, data in data.items():
	    ax.plot(data[0], data[1], 'o', color = styles[group], label=group)

	ax.legend()
	plt.title("Sepal Length vs Petal Length") 
	plt.xlabel('Sepal Length') 
	plt.ylabel('Petal Length') 
	plt.show()
	plt.savefig("Sepal Length vs Petal Length")

	################################
	# sepal length vs. petal width #
	################################
	data = {"setosa": [setosa[:,0], setosa[:,3]], 
    		"versicolor": [versicolor[:,0], versicolor[:,3]],
    		"virginica": [virginica[:,0], virginica[:,3]]}

	styles = {"setosa": 'b', 
			"versicolor": 'c',
			"virginica": 'r'}

	fig, ax = plt.subplots()

	for group, data in data.items():
	    ax.plot(data[0], data[1], 'o', color = styles[group], label=group)

	ax.legend()
	plt.title("Sepal Length vs Petal Width") 
	plt.xlabel('Sepal Length') 
	plt.ylabel('Petal Width') 
	plt.show()
	plt.savefig("Sepal Length vs Petal Width")

	################################
	# sepal width vs. petal length #
	################################
	data = {"setosa": [setosa[:,1], setosa[:,2]], 
			"versicolor": [versicolor[:,1], versicolor[:,2]],
			"virginica": [virginica[:,1], virginica[:,2]]}

	styles = {"setosa": 'b', 
			"versicolor": 'c',
			"virginica": 'r'}

	fig, ax = plt.subplots()

	for group, data in data.items():
	    ax.plot(data[0], data[1], 'o', color = styles[group], label=group)

	ax.legend()
	plt.title("Sepal Width vs Petal Length") 
	plt.xlabel('Sepal Width') 
	plt.ylabel('Petal Length') 
	plt.show()
	plt.savefig("Sepal Width vs Petal Length")

	###############################
	# sepal width vs. petal width #
	###############################
	data = {"setosa": [setosa[:,1], setosa[:,3]], 
			"versicolor": [versicolor[:,1], versicolor[:,3]],
			"virginica": [virginica[:,1], virginica[:,3]]}

	styles = {"setosa": 'b', 
			"versicolor": 'c',
			"virginica": 'r'}

	fig, ax = plt.subplots()

	for group, data in data.items():
	    ax.plot(data[0], data[1], 'o', color = styles[group], label=group)

	ax.legend()
	plt.title("Sepal Width vs Petal Width") 
	plt.xlabel('Sepal Width') 
	plt.ylabel('Petal Width') 
	plt.show()
	plt.savefig("Sepal Width vs Petal Width")

	################################
	# petal length vs. petal width #
	################################
	data = {"setosa": [setosa[:,2], setosa[:,3]], 
			"versicolor": [versicolor[:,2], versicolor[:,3]],
			"virginica": [virginica[:,2], virginica[:,3]]}

	styles = {"setosa": 'b', 
			"versicolor": 'c',
			"virginica": 'r'}

	fig, ax = plt.subplots()

	for group, data in data.items():
	    ax.plot(data[0], data[1], 'o', color = styles[group], label=group)

	ax.legend()
	plt.title("Petal Length vs Petal Width") 
	plt.xlabel('Petal Length') 
	plt.ylabel('Petal Width') 
	plt.show()
	plt.savefig("Petal Length vs Petal Width")

	return None
