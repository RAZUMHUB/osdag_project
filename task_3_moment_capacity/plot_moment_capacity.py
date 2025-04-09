import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("moment_capacity_data.xlsx")
sections = df["Beam Section"]
capacities = df["Moment Capacity"]

plt.figure(figsize=(8, 5))
plt.bar(sections, capacities, color='orange')
plt.xlabel("Beam Section")
plt.ylabel("Moment Capacity (kNm)")
plt.title("Moment Capacity of Different Beam Sections")
plt.tight_layout()
plt.savefig("output_plots/moment_capacity_plot.png")
print("✅ Moment capacity plot saved in output_plots/")
