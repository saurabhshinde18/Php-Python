import pandas as pd

# Load the CSV file into a pandas DataFrame
data = pd.read_csv("C:\\Users\\shind\\OneDrive\\Desktop\\python+php\\slip no 11\\winequality-red.csv")

# Display basic statistical details of the data
summary = data.describe()

# Print the summary statistics
print(summary)
