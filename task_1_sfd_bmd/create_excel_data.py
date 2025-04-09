import pandas as pd

# Define data
data = {
    "Position": [0, 1, 2, 3, 4, 5],
    "Shear Force": [0, 10, 10, -5, -5, 0],
    "Bending Moment": [0, 10, 20, 15, 5, 0]
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel("sfd_bmd_data.xlsx", index=False)

print("Excel file created successfully.")
