import numpy as np
import matplotlib.pyplot as plt

# Generate a random array of 50 integers between 0 and 100
random_integers = np.random.randint(0, 100, 50)

# Create a figure with subplots for line chart and scatter plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Line chart
ax1.plot(random_integers, marker='o', linestyle='-', color='b', label='Random Integers')
ax1.set_title('Line Chart')
ax1.set_xlabel('Index')
ax1.set_ylabel('Value')
ax1.legend()

# Scatter plot
x = np.arange(1, 51)  # Create an array for x values (1 to 50)
ax2.scatter(x, random_integers, c='r', marker='s', label='Random Integers')
ax2.set_title('Scatter Plot')
ax2.set_xlabel('Index')
ax2.set_ylabel('Value')
ax2.legend()

# Add a common title for both subplots
plt.suptitle('Random Integer Data Visualization', fontsize=16)

# Display the plots
plt.tight_layout()
plt.show()
