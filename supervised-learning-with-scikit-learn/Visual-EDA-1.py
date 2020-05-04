# Election votes are loaded as df
# Seaborn is imported as sns
# Matplotlib.pyplot is imported as plt

plt.figure()
sns.countplot(x='education', hue='party', data=df, palette='RdBu')
plt.xticks([0,1], ['No', 'Yes'])
plt.show()