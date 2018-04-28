
a = raw_input("\nA:")

a = a.split(",")

for i in range(len(a)-1):
    smallest = i
    for j in range(i+1, len(a)):
        if a[j] < a[smallest]:
            smallest = j
    temp = a[i]
    a[i] = a[smallest]
    a[smallest] = temp
print a
