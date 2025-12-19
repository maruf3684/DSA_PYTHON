nums = [1,3,5,4,7]

def longest(nums):
    start = 0
    end = 0
    maxi = 0
    while end < len(nums):
        if start  ==  end:
            end +=1
        else:
            if nums[end] > nums [end-1]:
                end+=1
            else:
                start = end
                continue

        val = end - start
        if val > maxi:
            maxi = val
            print(start, end)

    return maxi


print(longest(nums))