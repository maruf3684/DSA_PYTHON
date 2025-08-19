x = 8



def find_squrt(x):
    left = 0
    right = x
    ans = -1

    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
            ans = mid

    if ans * ans > x:
        return ans -1
    else:
        return ans

print(find_squrt(x))