# to fix
def main():
    t = input()
    for i in range(t):
        C, D, L = map(int, raw_input().split())
        if L % 4 != 0:
            print "no"
        elif 4 * (C + D) == L:
            print "yes"
        elif 4 * D == L:
            print "yes"
        elif 4 * C == L:
            print "yes"
        elif (4 * D) < L and L <= 4 * (C + D):
            print "yes"
        else:
            print "no"

if __name__ == '__main__':
    main()
