import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_excel("beam_data.xlsx") 
positions = df["Position"] 
shear_force = df["Shear Force"] 
bending_moment = df["Bending Moment"] 
