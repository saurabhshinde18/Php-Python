import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42) 
data = np.random.randint(1, 100, 50)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(data, color='blue', marker='o', linestyle='-')
axes[0, 0].set_title('Line Chart')
axes[0, 0].set_xlabel('Data Point')
axes[0, 0].set_ylabel('Value')

axes[0, 1].scatter(range(len(data)), data, color='green', marker='x')
axes[0, 1].set_title('Scatter Plot')
axes[0, 1].set_xlabel('Data Point')
axes[0, 1].set_ylabel('Value')

axes[1, 0].hist(data, bins=10, color='purple', alpha=0.7)
axes[1, 0].set_title('Histogram')
axes[1, 0].set_xlabel('Value')
axes[1, 0].set_ylabel('Frequency')

axes[1, 1].boxplot(data, vert=False, patch_artist=True)
axes[1, 1].set_title('Box Plot')
axes[1, 1].set_yticklabels([])
axes[1, 1].set_xlabel('Value')

fig.suptitle('Random Data Visualization', fontsize=16)

plt.tight_layout()

plt.show()
