import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('C:\\Users\\shind\\OneDrive\\Desktop\\python+php\\slip no 8\\winequality-red.csv')

# Separate the target variable (quality) from the features
X = data.drop('quality', axis=1)

# Standardize the features using StandardScaler
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

# Create a new DataFrame with the standardized features
X_standardized_df = pd.DataFrame(X_standardized, columns=X.columns)

# Concatenate the standardized features with the target variable
final_data = pd.concat([X_standardized_df, data['quality']], axis=1)

# Save the standardized data to a new CSV file
final_data.to_csv('winequality-red-standardized.csv', index=False)

print("Data standardization completed and saved as 'winequality-red-standardized.csv'")
