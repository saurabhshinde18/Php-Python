import pandas as pd

file_path = 'C:\\Users\\shind\\OneDrive\\Desktop\\python+php\\slip no 4\\User_Data.csv'

df = pd.read_csv(file_path)

num_rows, num_columns = df.shape

data_types = df.dtypes
feature_names = df.columns.tolist()

data_description = df.describe()

print(f"Shape of the data: {num_rows} rows x {num_columns} columns")
print("\nData Types:")
print(data_types)
print("\nFeature Names (Column Names):")
print(feature_names)
print("\nData Description:")
print(data_description)
