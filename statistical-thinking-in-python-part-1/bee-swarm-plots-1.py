#Make a bee swarm plot of the iris petal lengths. Your x-axis should contain each of the three species, and the y-axis the petal lengths. A data frame containing the data is in your namespace as df.

# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(data = df, x = 'species', y = 'petal length (cm)')

# Label the axes
_ = plt.xlabel('Species')
_ = plt.ylabel('Petal length (cm)')

# Show the plot
plt.show()