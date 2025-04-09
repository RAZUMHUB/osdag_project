import pandas as pd
import matplotlib.pyplot as plt
import os

# Load Excel file
file_path = "sfd_bmd_data.xlsx"

df = pd.read_excel(file_path)

# Check column names
print("Columns in Excel:", df.columns.tolist())

# Adjust these if column names are different
x = df['Position']
sfd = df['Shear Force']
bmd = df['Bending Moment']

# Create output directory
output_dir = "output_plots"
os.makedirs(output_dir, exist_ok=True)

# Plot SFD
plt.figure(figsize=(10, 5))
plt.plot(x, sfd, color='blue', linewidth=2)
plt.title("Shear Force Diagram")
plt.xlabel("Position (m)")
plt.ylabel("Shear Force (kN)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.savefig(f"{output_dir}/SFD_plot.png")
plt.close()

# Plot BMD
plt.figure(figsize=(10, 5))
plt.plot(x, bmd, color='red', linewidth=2)
plt.title("Bending Moment Diagram")
plt.xlabel("Position (m)")
plt.ylabel("Bending Moment (kNm)")
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.savefig(f"{output_dir}/BMD_plot.png")
plt.close()

print("✅ SFD and BMD plots saved to:", output_dir)
