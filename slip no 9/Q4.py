import pandas as pd

# a) Import the dataset and describe it
data = pd.read_csv('C:\\Users\\shind\\OneDrive\\Desktop\\python+php\\slip no 9\\winequality-red.csv')
description = data.describe()

# b) Display the shape of the dataset
shape = data.shape

# c) Display the first 3 rows from the dataset
first_3_rows = data.head(3)

# Display the results
print("a) Description of the dataset:")
print(description)
print("\nb) Shape of the dataset:", shape)
print("\nc) First 3 rows from the dataset:")
print(first_3_rows)
