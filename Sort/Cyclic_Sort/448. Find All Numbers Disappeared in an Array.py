def missing_number(arr):
    i = 0
    n = len(arr)
    ans = []
    while i<n:
        item = arr[i]
        need_to_be = i+1
        if item == need_to_be or item > n or item == arr[item-1]:
            i+=1
        else:
            arr[item-1],arr[i] = arr[i],arr[item-1]

    for index,item in enumerate(arr):
        if index+1 != item:
            ans.append(index+1)
    return [] if len(ans)==0 else ans



print(missing_number([4,3,2,7,8,2,3,1]))
print(missing_number([0,1]))

