import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)

# Get basic information
print("\nInfo:")
print(df.info())

# Describe numerical columns
print("\nDescription:")
print(df.describe())

# Select a column
print("\nAges:")
print(df['Age'])

print(df)
print("dataframe succesfully dispalyed")
