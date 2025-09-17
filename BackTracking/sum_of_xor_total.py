from functools import reduce

nums = [5,1,6]


def sum_of_xor_total(nums,i,list,ans):
    if i<0:
        xor_val = reduce(lambda a, b: a ^ b, list, 0)
        ans[0] += xor_val
    else:
        pick = [*list,nums[i]]
        non_pick = [*list]

        sum_of_xor_total(nums,i-1,pick,ans)
        sum_of_xor_total(nums,i-1,non_pick,ans)
    return ans[0]


print(sum_of_xor_total(nums,nums.__len__()-1,[],[0]))