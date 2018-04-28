a = raw_input()
a = list(a)
x = raw_input()

def main(a, x):
    last = a[-1]
    a[-1] = x
    i = 0
    while a[i] != x:
        i+=1
    a[-1] = last
    if i < len(a)-1 or a[-1]==x:
        return i
    return "Not Found"
print(main(a,x))
