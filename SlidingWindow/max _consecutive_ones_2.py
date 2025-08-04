nums = [1,0,1,1,0,1]
#ans = 4 As u can make one 0 to one


ptr1 = 0
ptr2 = 0
count = 0
if nums[0] == 1:
    count += 1

lifeIndex = None

while ptr2 < len(nums):
    if nums[ptr2] == 1:
        count = max(count, ptr2 - ptr1 + 1)
        ptr2 += 1
    elif nums[ptr2] == 0:
        if lifeIndex is None:
            count = max(count, ptr2 - ptr1 + 1)
            lifeIndex = ptr2
            ptr2 += 1
        else:
            ptr1  = lifeIndex+1
            lifeIndex = ptr2
            ptr2 += 1

print(count)