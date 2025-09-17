nums = [1,2,3]

#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



def make_permutations(nums,i,sub_array,ans):
    if i == 0:
        ans.append([*sub_array])
        return
    for item in range(0,i,-1):
        sub_array.append(nums[item])
        make_permutations(nums,i-1,sub_array,ans)
        sub_array.pop()

    return ans


print(make_permutations(nums,nums.__len__(),[],[]))