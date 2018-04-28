
def main():
    t = input()
    for i in range(t):
        H, C, Ts = map(float, raw_input().split())
        c1 = H > 50
        c2 = C < 0.7
        c3 = Ts > 5600
        if c1 and c2 and c3:
            print("10")
        elif c1 and c2:
            print("9")
        elif c2 and c3:
            print("8")
        elif c1 and c3:
            print("7")
        elif (c1 and not c2 and not c3) or (c2 and not c1 and not c3) or (c3 and not c1 and not c2):
            print("6")
        elif not c1 and not c2 and not c3:
            print("5")
        else:
            pass

if __name__ == '__main__':
    main()
