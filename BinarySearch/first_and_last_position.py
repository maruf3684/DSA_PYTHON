nums = [5,7,7,8,8,8,10]
target = 8

nums = [1]
target = 1

def find_first_last(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            right = mid
            left = mid
            while left >=0 and nums[left] == target:
                left -= 1
            while right < len(nums) and nums[right] == target:
                right += 1
            return left+1, right-1

        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

print(find_first_last(nums, target))



def find_first_last_2(nums, target,find_left):
    low = 0
    high = len(nums) - 1
    element = -1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            element = mid
            if find_left:
                high = mid - 1
            else:
                low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return element

left = find_first_last_2(nums, target, True)
right = find_first_last_2(nums, target, False)
print(left, right)