import pandas as pd 
df = pd.read_csv("beam_data.csv") 
df.to_excel("beam_data.xlsx", index=False) 
