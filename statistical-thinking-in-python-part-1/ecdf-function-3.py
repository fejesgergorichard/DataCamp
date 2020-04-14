# Compute ECDFs

# Setosa 
x_set, y_set = ecdf(setosa_petal_length)

# Versicolor
x_vers, y_vers = ecdf(versicolor_petal_length)

# Virginica
x_virg, y_virg = ecdf(virginica_petal_length)

# Plot all ECDFs on the same plot
_ = plt.plot(x_set, y_set)
_ = plt.plot(x_vers, y_vers)
_ = plt.plot(x_virg, y_virg)

# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()