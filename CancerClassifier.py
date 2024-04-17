from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

breast_cancer_data = load_breast_cancer()

# Split the data into training and testing sets
training_data, validation_data, \
    training_labels, validation_labels = \
    train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size=0.2, random_state=100)

def distance(point1, point2):
    """
    Calculates the distance between 2 data points
    """
    difference = 0
    for i in range(len(point1)):
        difference += (point1[i] - point2[i]) ** 2
    real_distance = difference ** 0.5
    return real_distance

def classify(data_point, dataset, labels, k):
    """
    :param data_point: data point to be classified
    :param dataset: dataset that the data point will be compared to
    :param labels: labels of the data set
    :param k: Number of closest points to compare the data point to
    :return: Classification of the data point. 0 if malignant, 1 if benign.
    """
    distances = []
    for item in range(len(dataset)):
        distance_between = distance(data_point, dataset[item])
        distances.append([distance_between, labels[item]])
    distances.sort()
    k_neighbors = distances[:k]

    num_malignant = 0
    num_benign = 0

    for point in k_neighbors:
        if point[1] == 0:
            num_malignant += 1
        else:
            num_benign += 1

    if num_benign > num_malignant:
        return 1
    else:
        return 0

def validation_accuracy(training_set, training_labels, validation_set, validation_labels, k):
    """
    Uses the classify method to guess the classification of the points in the validation set. Returns the fractional
    accuracy of the classify method (between 0 and 1).
    """
    correct = 0
    for point in range(len(validation_set)):
        test = classify(validation_set[point], training_set, training_labels, k)
        if test == validation_labels[point]:
            correct += 1
    return (correct/len(validation_set))

accuracies = []
k_range = range(1, 101)


for k in k_range: # Create a list of accuracies for a range of k values from 1 to 100.
    new_accuracy = validation_accuracy(training_data, training_labels, validation_data, validation_labels, k)
    accuracies.append(new_accuracy)

# Create a graph of Accuracy vs K
plt.xlabel('k')
plt.ylabel('Validation Accuracy')
plt.title('Breast Cancer Classifier Accuracy')
plt.plot(k_range, accuracies)
plt.show()


