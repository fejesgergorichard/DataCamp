# n-fold cross-validation is a method of sorting out the error in the fitting of our models that is caused by the train-test split.
# Sometimes the split of the data causes the fit to be biased, so we use cross-validation
# 3-fold cross-validation for example would be splitting the data to 2/3 training and 1/3 test
# But instead of doing this one time, we use every third of the data for 3 occasions and test all folds.
# scikit-learn's cross_val_score() function uses the R^2 as the metric of scope. 

# Import the necessary modules
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

# Create a linear regression object: reg
reg = LinearRegression()

# Compute 5-fold cross-validation scores: cv_scores
# cross_val_score(estimator object using the fit, X, y, cv (number of samples which is 3 by default)
cv_scores = cross_val_score(reg, X, y, cv = 5)

# Print the 5-fold cross-validation scores
print(cv_scores)

print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))
