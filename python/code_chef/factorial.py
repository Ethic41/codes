t = input()
for i in range(t):
    N = input()
    A = 1
    while N > 1:
        A *= N
        N -= 1
    A = str(A)
    counter = 0
    z = -1
    while A[z] == "0":
        counter +=1
        z -=1
    print counter
