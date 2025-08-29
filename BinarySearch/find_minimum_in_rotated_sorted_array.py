arr = [4,5,6,7,0,1,2]

arr = [8,4,6,7]

def find_min(arr):
    left = 0
    right = len(arr)-1

    if arr[left] < arr[right]:
        return arr[left]

    while left<right:
        mid = left + (right-left)//2
        if arr[mid] > arr[right]:
            left = mid+1
        elif arr[mid] <= arr[right]:
            right = mid
    return arr[left]


## rool of thumb : move to vengence area



print(find_min(arr))