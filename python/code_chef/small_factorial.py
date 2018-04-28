t = input()
for i in range(t):
    N = input()
    A = 1
    while N > 1:
        A *= N
        N -= 1
    print A
