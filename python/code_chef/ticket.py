def main(S):
    if S[0]==S[1]:
        return "NO"
    c = S[0]
    for i in range(2,len(S),2):
        if c != S[i]:
            return "NO"
        c = S[i]
        print(c)
    return "YES"
T = input()
for i in range(T):
    S = raw_input()
    print(main(S))
