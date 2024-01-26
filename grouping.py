import pandas as pd

# List of file paths
file_paths = [
    "Coast.xlsx",
    "Pant.xlsx",
    "Sweet.xlsx",
    "Tshirt.xlsx"
]

# Create an empty DataFrame to store the combined data
combined_data = pd.DataFrame()

# Read each Excel file and append its data to the combined DataFrame
for file_path in file_paths:
    data = pd.read_excel(file_path)
    # Add a new column with the name of the file
    data['Type'] = file_path.split('.')[0]
    combined_data = pd.concat([combined_data, data], ignore_index=True)

# Write the combined data to a new Excel file
combined_data.to_excel("Clothes.xlsx", index=False)
