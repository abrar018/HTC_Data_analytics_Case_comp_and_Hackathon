import pandas as pd

# Load the CSV files with their respective encodings
df_gas = pd.read_csv('gas_plants_negative_longitude.csv', encoding='utf-8')
df_ghg = pd.read_csv('GHGdataset.csv', encoding='latin2')

# Round the Latitude and Longitude columns to 2 decimal places in both dataframes
df_gas['Latitude'] = df_gas['Latitude'].round(2)
df_gas['Longitude'] = df_gas['Longitude'].round(2)
df_ghg['Latitude'] = df_ghg['Latitude'].round(2)
df_ghg['Longitude'] = df_ghg['Longitude'].round(2)

# Merge df_ghg (GHGdataset) with df_gas on Latitude and Longitude.
# This will add the "Unique Facility ID" from df_gas to df_ghg where the lat/long match.
merged_df = pd.merge(
    df_ghg,
    df_gas[['Unique Facility ID', 'Latitude', 'Longitude']],
    on=['Latitude', 'Longitude'],
    how='left'
)

# Reorder the columns to move "Unique Facility ID" to the beginning, if it exists.
cols = merged_df.columns.tolist()
if "Unique Facility ID" in cols:
    cols.remove("Unique Facility ID")
    merged_df = merged_df[["Unique Facility ID"] + cols]
else:
    print("Warning: 'Unique Facility ID' column not found in the merged DataFrame.")

# Save the merged DataFrame to a new CSV file with Latin2 encoding (to match GHGdataset)
merged_df.to_csv('GHGdataset_with_facility_id.csv', index=False, encoding='latin2') 