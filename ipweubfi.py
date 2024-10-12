import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("strong.csv")
exercises = df["Exercise Name"].unique()

count = 0
for i in exercises:
    print(f"{count+1}: {i}")
    count += 1


x = int(input("Choose exercise: "))
while x < 1 or x > len(exercises):
    print("Invalid index! ")
    x = int(input("Choose exercise: "))

data = df.loc[df["Exercise Name"] == exercises[x-1]]
data = data.sort_values(by=["Set Order"])
data.plot.scatter(x='Weight', y='Reps', title = exercises[x-1])
plt.show()