nums = [0,0,1,1,1,2,2,3,3,4]
#Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]


def remove_duplicate(nums):
    start = 0
    end = 0

    while end < len(nums):
        if nums[start] == nums[end]:
            end+=1
        else:
            start+=1
            nums[start] = nums[end]

    print(start)
    print(nums)
    return start+1


remove_duplicate(nums)