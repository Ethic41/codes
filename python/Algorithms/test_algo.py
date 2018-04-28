#this is a test implementation of sentinel search
"""
A ===> array to search
x ===> character to search for
n ===> length of array
"""
def main(A, x):
    n = len(A)
    result = sentinel(A, x, n)
    return "%d was found at position %d"%(x, result)
def sentinel(A, x, n):
    last = A[-1] #take the last element in the array and store it, the sentinel
    A[-1] = x #put the value we are searching 4 in the last place in Array
    i = 0
    while(A[i] != x):
        i += 1
    A[-1] = last
    if (i+1 < n) | (A[-1] == x):
        return i
    else:
        print("NOT FOUND")
        exit()

A = [3,5,2,6,7,8,3,7,8,1,7,8,34,67,8,656,970,87,23,52,632,65]
x = 2
print(main(A, x))
