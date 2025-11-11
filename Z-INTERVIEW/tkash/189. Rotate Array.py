nums = [1,2,3,  4,5,6,7,8,9,10]
#7654 321
k = 4
#Output: [5,6,7,1,2,3,4]

def rotate(nums,k):
    k = k % len(nums)
    print(k)
    start = 0
    end = len(nums) - k -1
    while start<end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1

    start = len(nums)-k
    end = len(nums)-1
    while start<end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1
    nums.reverse()
    print(nums)



rotate(nums,k)