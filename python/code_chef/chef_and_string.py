string = raw_input()
c = 0
h = 0
e = 0
f = 0
for i in string:
    if i == "C":
        c+=1
    elif i == "H" and c > h:
        h+=1
    elif i == "E" and h > e:
        e+=1
    elif i == "F" and e > f:
        f+=1
print min([c,h,e,f])
