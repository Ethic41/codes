S = raw_input()
N = input()
for i in range(N):
    Wi = raw_input()
    c = 0
    for x in Wi:
        if x in S:
            c+=1
        else:
            print("No")
            break
    if c == len(Wi):
        print("Yes")
