# Accuracy is not always an informative metric. e.g.: about 1% of emails are spam, but if we do not
# mark any email as spam, we would still have a 99% accuracy
# Thus, we compute a confusion matrix (true positives, true negatives, false positives, false negatives)
# and we generate a classification report.

# In these exercises we will work with the PIMA Indians dataset obtained from the UCI Machine Learning Repository
# The goal is to predict whether or not a given female patient will contract diabetes based on features such as BMI, age, and number of pregnancies.
# This is a binary classification problem. A target value of 0 indicates that the patient does not have diabetes
# a target value of 1 indicates that the patient does have diabetes.
# The dataset has been loaded into DataFrame 'df', and the feature and target variable arrays are created as 'X' and 'y'. 


# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


# Create training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 42)

# Instantiate a k-NN classifier: knn
knn = KNeighborsClassifier(n_neighbors = 6)

# Fit the classifier to the training data
knn.fit(X_train, y_train)

# Predict the labels of the test data: y_pred
y_pred = knn.predict(X_test)

# Generate the confusion matrix and classification report
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
