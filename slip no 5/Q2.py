import pandas as pd

file_path = 'C:\\Users\\shind\\OneDrive\\Desktop\\python+php\\slip no 5\\User_Data.csv'

data = pd.read_csv(file_path)

# Print the shape (number of rows and columns)
print('Shape of the data:', data.shape)
print('Number of rows:', data.shape[0])
print('Number of columns:', data.shape[1])

# Print the data types of each column
print('\nData types of each column:')
print(data.dtypes)

# Print the feature names
print('\nFeature names:')
print(list(data.columns))

# Print the description of the data
print('\nDescription of the data:')
print(data.describe())