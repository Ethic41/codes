
inp = input()
def fac(inp):
    if inp == 0:
        return 1
    else:
        return inp * fac(inp-1)
print(fac(inp))
