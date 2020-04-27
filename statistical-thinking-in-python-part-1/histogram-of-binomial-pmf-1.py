# Compute bin edges: bins
bins = np.arange(0, max(n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults, bins = bins, normed = True)

# Label axes
plt.xlabel("X")
plt.ylabel("Y")

# Show the plot
plt.show()
