

def missing_number(arr):
    i = 0
    n = len(arr)

    while i<n:
        item = arr[i]
        if item == i or item >= n:
            i+=1
        else:
            arr[item],arr[i] = arr[i],arr[item]

    for index,item in enumerate(arr):
        if index != item:
            return index
    return len(arr)



print(missing_number([9,6,4,2,3,5,7,0,1]))
print(missing_number([0,1]))