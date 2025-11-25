import pandas as pd
import os
from glob import glob

# Path to the Data folder
data_path = '../Data/'

# List of month folders
months = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

# Initialize list to store DataFrames
all_dfs = []

# Loop through each month folder
for month in months:
    folder_path = os.path.join(data_path, month)
    
    # Get the cleaned CSV file(s) in the folder
    cleaned_files = glob(os.path.join(folder_path, 'Divvy_cleaned_*_2024.csv'))
    
    # Loop through cleaned files and read them
    for file in cleaned_files:
        print(f'Reading {file}')
        df = pd.read_csv(file)
        all_dfs.append(df)

# Concatenate all DataFrames
merged_data = pd.concat(all_dfs, ignore_index=True)

# Optional: save the merged dataset
merged_data.to_csv(os.path.join(data_path, 'Divvy_2024_All_Months_Cleaned.csv'), index=False)

print('Merged dataset shape:', merged_data.shape)
print('Saved merged file to Divvy_2024_All_Months_Cleaned.csv')
