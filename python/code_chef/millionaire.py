t = input()
for i in range(t):
    N = input()
    A = raw_input()
    B = raw_input()
    cash = map(int, raw_input().split())
    c = 0
    for x in range(N):
        if A[x] == B[x]:
            c += 1
    if c == N:
        print cash[c]
    else:
        print cash[:c+1]

main()
