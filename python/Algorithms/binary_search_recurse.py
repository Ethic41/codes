def main():
    a = raw_input("a:")
    a = a.split(",")
    print(a)
    x = input("x:")
    r = len(a)
    p = 1
    recurse(a, p, r, x)


def recurse(a, p, r, x):
    if p > r:
        return "Not found"
    else:
        q = (p+r)/2
        print(q, x, p, r)

        if int(a[q]) == x:
            return q
        elif int(a[q]) > x:
            return recurse(a, p, q-1, x)
        elif int(a[q]) < x:
            return recurse(a, q+1, r, x)


if __name__ == "__main__":
    print(main())
