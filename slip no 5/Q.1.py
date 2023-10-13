import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers
random_array = np.random.randint(0, 100, 50)

# Line chart
plt.figure()
plt.plot(random_array, color='blue')
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

# Scatter plot
plt.figure()
plt.scatter(range(len(random_array)), random_array, color='red')
plt.title('Scatter Plot')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

# Histogram
plt.figure()
plt.hist(random_array, bins=10, color='green', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# Box plot
plt.figure()
plt.boxplot(random_array, vert=False)
plt.title('Box Plot')
plt.xlabel('Value')
plt.show()