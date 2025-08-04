# nums = [1,1,1,0,0,0,1,1,1,1,0]
# k = 2
#ANS=6

nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

# nums = [0,0,1,1,1,0,0]
# k=0

# nums = [1,1,1,0,0,0,1,1,1,1]
# k=0

from queue import Queue
ptr1 = 0
ptr2 = 0
count = 0
q = Queue()

while ptr2 < len(nums):
    if nums[ptr2] == 1:
        count = max(count, ptr2 - ptr1 + 1)
        ptr2 += 1
    elif nums[ptr2] == 0:
        if k != 0:
            k = k - 1
            count = max(count, ptr2 - ptr1 + 1)
            q.put(ptr2)
        else:
            if q.empty():
                ptr1 = ptr2 + 1
            else:
                item = q.get()
                if nums[item]+1 == 1:
                    ptr1 = item + 1
                else:
                    ptr1 = item + 1
                    q.get()
                q.put(ptr2)
        ptr2 += 1

print(count)