import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the CSV data
file_path = r'C:\Users\shind\OneDrive\Desktop\python+php\slip no 7\data.csv'  # Replace with the actual path to your CSV file
df = pd.read_csv(file_path)

# Task a: Apply One-Hot encoding on the "Country" column
# Create an instance of OneHotEncoder
encoder = OneHotEncoder(sparse=False, drop='first')  # 'drop' removes one category to prevent multicollinearity

# Fit and transform the "Country" column
country_encoded = encoder.fit_transform(df[['Country']])

# Get the feature names after one-hot encoding
feature_names = encoder.get_feature_names_out(['Country'])

# Create a DataFrame for the one-hot encoded "Country" column with proper column names
country_encoded_df = pd.DataFrame(country_encoded, columns=feature_names)

# Task b: Apply Label encoding on the "Purchased" column
# Create an instance of LabelEncoder
label_encoder = LabelEncoder()

# Encode the "Purchased" column
df['Purchased'] = label_encoder.fit_transform(df['Purchased'])

# Print the resulting DataFrame with one-hot encoded "Country" and label encoded "Purchased" columns
print("DataFrame with Encoded Columns:")
print(df)

# Save the updated DataFrame to a new CSV file
output_file_path = 'Encoded_Data.csv'  # Replace with the desired output file path
df.to_csv(output_file_path, index=False)
