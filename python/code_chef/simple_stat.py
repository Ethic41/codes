T = input()
for i in range(T):
    N, K = map(int, raw_input().split())
    A = map(int, raw_input().split())
    if K > 0:
        for i in range(K):
            A.remove(max(A))
            A.remove(min(A))
    print("%6f"%(sum(A)/float(len(A))))
