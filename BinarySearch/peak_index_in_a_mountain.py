arr = [2,4,6,8,10,8,5,4]
#arr = [0,10,5,2]

def peak_index(arr):
    ans = -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if mid < len(arr) and arr[mid] < arr[mid+1]:
            ans = mid+1
            left = mid+1
        elif mid > -1 and arr[mid] < arr[mid-1]:
            ans = mid-1
            right = mid-1
        else:
            ans = arr[mid]
            break




    return ans




print(peak_index(arr))