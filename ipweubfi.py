import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

#overtime you would expect the trend line to be around the targeted rep range
#how do you figure out if two lines are the same?

df = pd.read_csv("workout-thing/strong.csv")
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

slope, intercept, r, p, std_err = stats.linregress(data["Weight"], data["Reps"])

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, data["Weight"]))


plt.scatter(data["Weight"], data["Reps"])
plt.plot(data["Weight"], mymodel)
#data.plot.scatter(x='Weight', y='Reps', title = exercises[x-1])
plt.show()