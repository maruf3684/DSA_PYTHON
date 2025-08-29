mountainArr = [1,2,3,4,5,3,1]
target = 3

def peak_index(arr):
    ans = -1
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2

        if mid < len(arr) and arr[mid] < arr[mid+1]:
            ans = mid+1
            left = mid+1
        elif mid > -1 and arr[mid] < arr[mid-1]:
            ans = mid-1
            right = mid-1
        else:
            ans = mid
            break
    return ans

def binary_search(arr,left,right,x):
    while left<=right:
        mid = left + (right-left)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid+1
        elif arr[mid] > x:
            right = mid -1
    return -1


def find(mountainArr,target):
    pick = peak_index(mountainArr)
    left_search = binary_search(mountainArr,0,pick,target)
    if left_search != -1:
        return left_search
    right_search = binary_search(mountainArr,pick,len(mountainArr),target)
    if right_search != -1:
        return right_search
    return -1


print(find(mountainArr,target))
