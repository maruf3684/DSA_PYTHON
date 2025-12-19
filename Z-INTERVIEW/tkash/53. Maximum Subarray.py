nums = [-2]


def largest_sum(nums):
    i = 0
    sum = 0
    max = float('-inf')
    while i < len(nums):
        sum = sum + nums[i]
        if sum > max:
            max = sum
        if sum <=0:
            sum = 0

        i+=1
    return max

print(largest_sum(nums))