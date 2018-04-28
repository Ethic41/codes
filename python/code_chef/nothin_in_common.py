
def main():
    t = input()
    for i in range(t):
        n, m = map(int,raw_input().split())
        A = raw_input().split()
        B = raw_input().split()
        c = 0
        for val in A:
            if val in B:
                c+=1
        print c

if __name__ == '__main__':
    main()
