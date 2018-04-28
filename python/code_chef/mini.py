def mini(lists):
    c_min = lists[0]
    for i in lists[1:]:
        if i < c_min:
            c_min = i
    return c_min

print(mini([19,2,3,4,12,44,6,3,78,2,5,7,9,23,89]))
