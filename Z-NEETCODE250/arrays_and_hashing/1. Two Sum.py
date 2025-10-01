def twoSum(nums, target):
    past = {}
    for index, item in enumerate(nums):
        need = target - item
        if need in past:
            return [index, past[need]]
        past[item] = index
    return [-1,-1]



print(twoSum(nums = [2,7,11,15], target = 9))