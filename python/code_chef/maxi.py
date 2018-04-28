def maxi(lists):
    c_max = lists[0]
    for i in lists[1:]:
        if i > c_max:
            c_max = i
    return c_max

print(maxi([19,2,3,4,12,44,6,3,78,2,5,7,9,23,89]))
