
#clic sort

def first_missing_positive(arr):
    my_searching_range = len(arr)
    i = 0

    while i < my_searching_range:
        item = arr[i]
        if item <= my_searching_range:
            existing_item = arr[item]
            arr[item] = item






print(first_missing_positive([6,7,8,1,2,3])) #1-6