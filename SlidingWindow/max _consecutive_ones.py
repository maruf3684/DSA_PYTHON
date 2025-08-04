nums = [1,0,1,1,0,1]

ptr1 = 0
ptr2 = 0

count = 0
if nums[0] == 1:
    count = 1
while ptr2<len(nums):
    if nums[ptr2] == 1:
        count = max(count, ptr2 - ptr1+1)
        ptr2+=1
    elif nums[ptr2] == 0:
        while ptr2<len(nums) and nums[ptr2] != 1:
            ptr2+=1
        ptr1 = ptr2


print(count)



