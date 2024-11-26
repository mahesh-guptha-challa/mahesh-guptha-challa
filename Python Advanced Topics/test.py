import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('my_file.csv')

# Find duplicate rows
df_duplicates = df[df.duplicated(keep=False)]

# Sort the DataFrame by the first column (assume column index 0)
df_duplicates_sorted = df_duplicates.sort_values(by=df.columns[0])

# Display the sorted DataFrame with duplicates
print(df_duplicates_sorted)
