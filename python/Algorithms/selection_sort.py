from time import time

a = [3,4,9,7,2,6,0,5]
n = len(a)

def sorts(a, n):
    for i in range(n):
        smallest = i
        for j in range(i+1, n):
            if int(a[j])<int(a[smallest]):
                smallest = j
        temp = a[i]
        a[i] = a[smallest]
        a[smallest] = temp
    return a

if __name__ == "__main__":
    print(sorts(a,n))
