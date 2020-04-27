# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(n = 100, p = 0.05, size = 10000)

# Compute CDF: x, y
x, y = ecdf(n_defaults)

# Plot the CDF with axis labels
plt.plot(x,y, marker =".", linestyle='none')
plt.xlabel("Number of defaults out of 100 loans")
plt.ylabel("CDF")

# Show the plot
plt.show()