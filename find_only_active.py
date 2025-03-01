import pandas as pd

# Read the CSV file (adjust the filename and encoding if necessary)
df = pd.read_csv('gas_plants_negative_longitude.csv', encoding='latin2')

# Filter the DataFrame to include only rows where Status is 'Active'
df_active = df[df['Status'] == 'Active']

# Save the filtered DataFrame to a new CSV file
df_active.to_csv('filtered_active.csv', index=False, encoding='utf-8')
