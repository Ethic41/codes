inp = input()
def loop(inp):
    if inp == 0:
        return 1
    else:
        a = inp
        while a > 1:
            inp *= a - 1
            a -= 1
        return inp
print(loop(inp))
