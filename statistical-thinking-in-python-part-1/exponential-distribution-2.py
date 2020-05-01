####
# Now, you'll use your sampling function to compute the waiting time to observe a no-hitter
# and hitting of the cycle. The mean waiting time for a no-hitter is 764 games, and the mean
# waiting time for hitting the cycle is 715 games.


#The Exponential distribution describes the waiting times between rare events
def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2
    
# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764, 715, 100000)

# Make the histogram
_ = plt.hist(waiting_times, bins = 100, histtype='step', normed = True)


# Label axes
_ = plt.xlabel('Waiting times')
_ = plt.ylabel('')

# Show the plot
plt.show()
