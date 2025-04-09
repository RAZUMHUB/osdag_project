import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
file_path = "sfd_bmd_data.xlsx"
df = pd.read_excel(file_path)

# Extract values
positions = df['Position']
shear_forces = df['Shear Force']
bending_moments = df['Bending Moment']

# Plot Shear Force Diagram
plt.figure(figsize=(10, 4))
plt.plot(positions, shear_forces, marker='o', color='blue', label='Shear Force')
plt.title('Shear Force Diagram (SFD)')
plt.xlabel('Position (m)')
plt.ylabel('Shear Force (kN)')
plt.grid(True)
plt.legend()
plt.savefig("output_plots/shear_force_diagram.png")
plt.close()

# Plot Bending Moment Diagram
plt.figure(figsize=(10, 4))
plt.plot(positions, bending_moments, marker='o', color='red', label='Bending Moment')
plt.title('Bending Moment Diagram (BMD)')
plt.xlabel('Position (m)')
plt.ylabel('Bending Moment (kNm)')
plt.grid(True)
plt.legend()
plt.savefig("output_plots/bending_moment_diagram.png")
plt.close()

print("✅ SFD & BMD plots saved successfully in output_plots/")
