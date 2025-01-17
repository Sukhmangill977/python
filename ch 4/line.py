# Plot a Line Graph

import matplotlib.pyplot as plt

# Sample Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotting the graph
plt.plot(x, y, label='Line Graph', color='blue')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Graph Example')
plt.legend()
plt.show()
