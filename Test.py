import pandas as pd
import glob

# Read all Excel files in the specified directory
excel_files = glob.glob("path_to_excel_files/*.xlsx")

# Initialize an empty list to store dataframes
dataframes = []

# Loop through the list of Excel files and read each one into a dataframe
for file in excel_files:
    try:
        df = pd.read_excel(file)
        dataframes.append(df)
    except Exception as e:
        print(f"Error reading {file}: {e}")

# Concatenate all dataframes into a single dataframe
try:
    combined_df = pd.concat(dataframes, ignore_index=True)
    # Print the combined dataframe
    print(combined_df)
except Exception as e:
    print(f"Error concatenating dataframes: {e}")