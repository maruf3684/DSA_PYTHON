def duplicate_number(arr):
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
        if index+1 != item and item == arr[item-1]:
            ans.append(item)
    return ans[0]



print(duplicate_number([1,3,4,2,2]))