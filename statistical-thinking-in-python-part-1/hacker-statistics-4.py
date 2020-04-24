# Compute ECDF: x, y (ecdf() function is available from previous exercises)
x, y = ecdf(n_defaults)

# Plot the ECDF with labeled axes
_ = plt.plot(x,y, marker = ".", linestyle = 'none')
_ = plt.xlabel('X')
_ = plt.ylabel('Y')

# Show the plot
plt.show()

# Compute the number of 100-loan simulations with 10 or more defaults: n_lose_money
n_lose_money = np.sum(n_defaults >= 10)

# Compute and print probability of losing money
print('Probability of losing money =', n_lose_money / len(n_defaults))
