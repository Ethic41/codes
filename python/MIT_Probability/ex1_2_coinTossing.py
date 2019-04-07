import random

coin = ["H", "T"]
outcomes = {"Heads":0, "Tails":0}
number_of_experiment = int(input("number of experiments:\n"))

for i in range(number_of_experiment):
    toss = random.choice(coin)
    if toss == "H":
        outcomes["Heads"] += 1
    else:
        outcomes["Tails"] += 1

print("====[ Heads = {} ]====".format(outcomes["Heads"]))
print("====[ Tails = {} ]====".format(outcomes["Tails"]))