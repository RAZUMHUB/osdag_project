import pandas as pd

df = pd.read_csv("moment_capacity_data.csv")
df.to_excel("moment_capacity_data.xlsx", index=False)

print("✅ CSV converted to Excel!")
