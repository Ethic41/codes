def main():
    s = input()
    for i in range(s):
        Ni = input()
        Hi = map(int, raw_input().split())
        left_part = Hi[:Ni/2+1]
        right_part = Hi[Ni/2:]
        cond1 = Ni % 2 != 0
        cond2 = Hi[0] == Hi[-1] == 1
        cond3 = check(left_part)
        cond4 = check(right_part,1)
        if cond1 and cond2 and cond3 and cond4:
            print("yes")
        else:
            print("no")

def check(seq, rev=0):
    if rev != 0:
        seq.reverse()
    num = 0
    for i in seq:
        if i - num != 1:
            return False
        num = i
    return True
main()
