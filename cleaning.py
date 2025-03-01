import pandas as pd

# Read the CSV file (change the filename as needed)
df = pd.read_csv('Geoscout Facility Data Dump.csv')

# Convert the "Date" column to datetime.
# Your dates are in "YYYY/MM" format (e.g., "1990/07"), so we specify the format.
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m', errors='coerce')

# Count how many rows have a failed date conversion (i.e., NaT in the "Date" column)
dropped_count = df['Date'].isna().sum()

# Drop any rows where Date conversion failed
df = df.dropna(subset=['Date'])

# Group by "Plant Name" and select the row with the latest date for each plant.
latest_df = df.loc[df.groupby('Plant Name')['Date'].idxmax()]

# Save the cleaned data to a new CSV file
latest_df.to_csv('gas_plants_latest.csv', index=False)

print("Cleaned data saved to 'gas_plants_latest.csv'")
print("Dropped rows due to failed date conversion:", dropped_count)
