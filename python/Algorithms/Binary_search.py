
def main():
    array = raw_input("array:").split(",")
    x = input("x:")
    n = len(array)
    p = 1
    r = n
    while p <= r:
        q = (p+r)/2
        print q
        if int(array[q-1]) == x:
            return "pos: "+str(q)
        elif int(array[q-1])>x:
            r = q-1
        elif int(array[q-1])<x:
            p = q+1
    return "Not Found"

print(main())
