"""
Ethan P. Gould
ethanpgould@gmail.com

"""
from create_data import create_data
from plot_data import plot_data
from integerize_labels import integerize_labels
from split import split
from euclidean_distance import euclidean_distance
from knn import knn
from weighted_knn import weighted_knn
from calculate_error_rate import calculate_error_rate

def compare_errors(k_vals, input_data_file):
    # TODO: 
    # read in the input data
    initial_data = create_data(input_data_file)

    # TODO:
    # create plots of the data (this should save the images within the current
    # directory)
    # plot_data(initial_data)

    # TODO:
    # integerize the data labels
    integerized_data, label_dict = integerize_labels(initial_data)

    # TODO:
    # split the data into train and test
    train, test = split(integerized_data)

    # TODO:
    ## compute the errors
    errors = {}
    for k in k_vals:
        predicted_labels = knn(train, test, k)
        error_rate = calculate_error_rate(predicted_labels, test)
        errors[k] = error_rate

    return errors

if __name__ == "__main__":
    k_vals = [1, 3, 5, 10, 15]
    # TODO: specify the filename
    input_data_file = 'iris.txt'
    errors = compare_errors(k_vals, input_data_file)
    for k in errors:
        print("Error value for k = %d was %f" % (k, errors[k]))
