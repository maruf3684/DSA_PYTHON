
#think about non value element

def remove_element(arr, val):
    k = 0
    for index,item in enumerate(arr):
        if item != val:
            arr[k] = item
            k += 1
    return arr[:k]




#print(remove_element([0,1,2,2,3,0,4,2],2))
print(remove_element([3,2,2,3],3))
print(remove_element([1,1,1,1],1))