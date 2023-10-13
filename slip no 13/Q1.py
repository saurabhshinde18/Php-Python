import numpy as np

flattened_array = np.array([1, 2, 3, 4, 5, 6])

array = flattened_array.reshape(2, 3)

weights = np.array([0.1, 0.2, 0.3])

axis = 1

weighted_avg = np.average(array, axis=axis, weights=weights)

print("Original array:")
print(array)

print("\nWeights:")
print(weights)

print("\nWeighted average along axis", axis, ":")
print(weighted_avg)