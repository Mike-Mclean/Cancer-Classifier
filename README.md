# Cancer Classifier

Uses a k-nearest neighbors algorithm to classify breast cancer data points. Creates a graph of "Accuracy vs K" to find optimal K value(s).

## How It Works:
**Tech used:** Python, scikit-learn, matplotlib 

The data is split into training and testing sets. The distance between the testing data points and the training datapoints is claculated. The k closest points are collected and the data point is classified as malignant if the majority of the k closest points are malignant. The data point will be classified as benign if the k closest points are benign.

The accuracy of the classifier is then calculated for many different value of k. The accuracies are plotted against k to vizualize k's affect on accuracy.
