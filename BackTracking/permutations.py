nums = [4,5,6]

#Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]



def make_permutations(nums,i,sub_array,ans,used):
    if i == 0:
        ans.append([*sub_array])
    else:
        for item in range(0,nums.__len__()):
            if used[item] == False:
                sub_array.append(nums[item])
                used[item] = True
                make_permutations(nums,i-1,sub_array,ans,used)
                sub_array.pop()
                used[item] = False
    return ans


print(make_permutations(nums,nums.__len__(),[],[],[False]*nums.__len__()))