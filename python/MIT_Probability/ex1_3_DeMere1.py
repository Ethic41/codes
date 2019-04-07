from random import choice as roll

dice = [1,2,3,4,5,6]
outcomes = {"six_obtained":0, "six_not_obtained":0}
number_of_experiment = int(input("number of experiment:\n"))

for i in range(number_of_experiment):
    six_obtained = False
    for i in range(4):
        toss = roll(dice)
        if toss == 6:
            outcomes["six_obtained"] += 1
            six_obtained = True
            break
    if not six_obtained:
        outcomes["six_not_obtained"] += 1

print("====[ six obtained = {} :: percentage = {}% ]====".format(outcomes["six_obtained"], outcomes["six_obtained"]/number_of_experiment * 100))
print("====[ six not obtained = {} :: percentage = {}% ]====".format(outcomes["six_not_obtained"], outcomes["six_not_obtained"]/number_of_experiment * 100))