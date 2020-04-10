# Import scikit learn
from sklearn.datasets import load_iris
# Import plotting modules
import seaborn as sns
import matplotlib.pyplot as plt

# Set default Seaborn style
sns.set()

# Plot histogram of versicolor petal lengths
plt.hist(versicolor_petal_length)
plt.xlabel('petal length (cm)')
plt.ylabel('count')

# Show histogram
plt.show()
