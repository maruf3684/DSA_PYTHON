
nums = [1,2,3,4]
# [24,12,8,6]

def product_of_self(nums):
    ans = [0]*len(nums)

    prefix = 1
    for i in range(0,len(nums)):
        ans[i] = prefix
        prefix = prefix*nums[i]

    print(ans)

    suffix = 1
    for i in range(len(nums)-1,-1,-1):
        ans[i] = suffix * ans[i]
        suffix = suffix * nums[i]

    print(ans)





    return ans










product_of_self(nums)