
list = [1,2,3,4,5,6,7,8,9,10,11,22,34]

def binary_search(list, target):
    left  = 0
    right = len(list) - 1

    while left <= right:
        mid  = left + (right - left) // 2

        if target == list[mid]:
            return mid, list[mid]
        elif target < list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1 ,-1

print(binary_search(list, 22))