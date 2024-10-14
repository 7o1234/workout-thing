import pandas as pd
import matplotlib.pyplot as plt 
from scipy import stats




df = pd.read_csv("workout-thing/strong.csv")
exercises = df["Exercise Name"].unique()

count = 0
for i in exercises:
    print(f"{count+1}: {i}")
    count += 1

choice = int(input("Choose exercise: "))
while choice < 1 or choice > len(exercises):
    print("Invalid index! ")
    choice = int(input("Choose exercise: "))
data = df.loc[df["Exercise Name"] == exercises[choice-1]]
data_weight = data[["Weight", "Reps"]]

print(data_weight)

