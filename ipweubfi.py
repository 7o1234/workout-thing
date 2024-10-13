import numpy as np 
import pandas as pd 
import seaborn as sns 
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

choice = int(input("Choose exercise: "))
while choice < 1 or choice > len(exercises):
    print("Invalid index! ")
    choice = int(input("Choose exercise: "))

data = df.loc[df["Exercise Name"] == exercises[choice-1]]
data_weight = data[["Weight", "Reps"]]

#plot two lines, straight line around rep range and one of linear regress
slope, intercept, r, p, std_err = stats.linregress(data_weight["Weight"], data_weight["Reps"])

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, data_weight["Weight"]))

plt.scatter(data_weight["Weight"], data_weight["Reps"])
plt.plot(data_weight["Weight"], mymodel)

#sns.lmplot(x="Weight", y="Reps", data = data_weight )
plt.show() 
