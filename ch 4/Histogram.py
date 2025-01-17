import matplotlib.pyplot as plt

# Sample Data
data = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

# Plotting the histogram
plt.hist(data, bins=10, color='green', edgecolor='black')
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.show()
