def first_missing_positive(arr):
    i = 0
    n = len(arr)
    while i<n:
        item = arr[i]
        need_to_be = i+1
        if item == need_to_be or item > n  or item<=0 or item == arr[item-1]:
            i+=1
        else:
            arr[item-1],arr[i] = arr[i],arr[item-1]

    for index,item in enumerate(arr):
        if index+1 != item:
            return index+1
    return len(arr)+1

print(first_missing_positive([1]))
print(
    first_missing_positive([-5])
)