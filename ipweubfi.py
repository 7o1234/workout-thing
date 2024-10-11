import pandas as pd


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
print(data)
