# Make a scatter plot
_ = plt.plot(versicolor_petal_length, versicolor_petal_width, marker='.', linestyle= 'none')


# Label the axes
_ = plt.xlabel('Petal Length')
_ = plt.ylabel('Petal Width')


# Show the result
_ = plt.show()
