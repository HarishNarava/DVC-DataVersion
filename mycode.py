import pandas as pd
import os

# Create a sample Dataframe with columns
data = {'Name': ['Alice', 'Harish', 'Charlie'],
       'Age': [25, 26, 35],
       'City': ['New York', 'Boston', 'Dallas']}

df = pd.DataFrame(data)

# # Adding a new row to df for V2
# new_row_loc = {'Name':'V2', 'Age': 28, 'City': 'Tampa'}
# df.loc[len(df.index)] = new_row_loc

# # Adding a new row to df for V3
# new_row_loc2 = {'Name':'V3', 'Age': 21, 'City': 'Tampa'}
# df.loc[len(df.index)] = new_row_loc2

# Ensuring that the data directory exists at the root level
data_dir = 'data'
os.makedirs(data_dir, exist_ok = True)

# Define the file path
file_path =  os.path.join(data_dir, 'sample_data.csv')

# Save the DataFrame to a CSV file, including the column names
df.to_csv(file_path, index=False)

print(f'CSV file saved to {file_path}')