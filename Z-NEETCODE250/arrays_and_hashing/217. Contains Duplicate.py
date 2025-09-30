def containsDuplicate(nums):
    tracker = {}
    for index,item in enumerate(nums):
        tracker[item] = tracker.get(item,0)+1
    for key,value in tracker.items():
        if value > 1:
            return True
    return False



print(containsDuplicate([1,2,3,1]))