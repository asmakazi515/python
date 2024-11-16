import pandas as pd

# Create a dictionary of data
data = {
    'Name': ['John', 'Jane', 'Mike', 'Sarah'],
    'Age': [25, 30, 28, 35],
    'City': ['New York', 'London', 'Paris', 'Sydney']
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print("Original DataFrame:")
print(df)
print()

# Accessing and manipulating data
print("Accessing and Manipulating Data:")
print("First two rows:")
print(df.head(2)) 
print()

print("Summary statistics:")
print(df.describe()) 
print()

print("Filtering data:")
filtered_df = df[df['Age'] > 28]  
print(filtered_df)
print()

# Adding a new column
df['Profession'] = ['Engineer', 'Doctor', 'Artist', 'Teacher']
print("DataFrame with a new column:")
print(df)
print()

# Grouping and aggregating data
grouped_df = df.groupby('Profession').mean() 
print("Grouped DataFrame:")
print(grouped_df)
print()

# Sorting the DataFrame
sorted_df = df.sort_values('Age', ascending=False)  
print("Sorted DataFrame:")
print(sorted_df)
