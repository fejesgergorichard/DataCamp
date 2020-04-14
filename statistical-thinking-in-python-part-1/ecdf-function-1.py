# Empirical cumulative distribution function (ECDF)
# The ecdf displays the distribution of data from 1/n to 1 in a range of the datasets values, where n is the number of data points

# On the Y axis we will see the values, for example the petal length ranging from 1 up to 7 mm
# The Y axis will show us the percentage or the percentile of that value in a range
# For example when we plot the ECDF for the famous petal length datase we get the following:
#  
#       ^ 
# 1.0   |           /                             *  
#       |          /                              *
# 0.7   |         /                              *
#       |        /                              *
# F     |       /                               *
# D     |      |                               *
# C     |      |                              *
# E     |      |                             *          --- setosa
#       |     /                              *          *** versicolor
# 0.2   |    /                               *
# 0.1   |   /                               *
# 0.0   -----|-----|-----|-----|-----|-----|-----|-----|-----|------->
#            1     2     3     4     5     6     7     8     9
#                             summary index 

# We can see from the graph above that 20% of the setosa petal lengths are 1 mm or shorter
# About 70% of the setosa petal lengths are 2 mm or shorter
# We can say that around 70% of the versicolor petals are 7 mm or shorter 


def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, n+1) / n

    return x, y
