from random import choice as roll

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]

outcomes = {"pair_of_six_obtained":0, "pair_of_six_not_obtained":0}
number_of_experiment = int(input("number of experiments:\n"))

for i in range(number_of_experiment):
    pair_of_six_obtained = False
    for j in range(24):
        toss_for_dice1 = roll(dice1)
        toss_for_dice2 = roll(dice2)
        if toss_for_dice1 == 6 and toss_for_dice2 == 6:
            outcomes["pair_of_six_obtained"] += 1
            pair_of_six_obtained = True
            break
    if not pair_of_six_obtained:
        outcomes["pair_of_six_not_obtained"] += 1

print("====[ pair of six obtained = {} :: percentage = {}% ]====".format(outcomes["pair_of_six_obtained"], outcomes["pair_of_six_obtained"]/number_of_experiment * 100))
print("====[ pair of six not obtained = {} :: percentage = {}% ]====".format(outcomes["pair_of_six_not_obtained"], outcomes["pair_of_six_not_obtained"]/number_of_experiment * 100))