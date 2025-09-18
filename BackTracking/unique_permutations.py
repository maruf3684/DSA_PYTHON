

nums = [1,1,2]


def unique_perms(nums,tracker,sub_arr,ans):
    if len(sub_arr) == len(nums):
        ans.append([*sub_arr])
    else:
        for i in range(len(nums)):
            if tracker[i]==True:
                continue
            if i > 0 and nums[i] == nums[i-1] and tracker[i-1] == False:
                continue

            sub_arr.append(nums[i])
            tracker[i]=True
            unique_perms(nums,tracker,sub_arr,ans)
            sub_arr.pop()
            tracker[i]=False
    return ans

print(unique_perms(sorted(nums),nums.__len__()*[False],[],[]))



# Call: sub_arr=[], tracker=[False, False, False]
# ├── pick nums[0]=1 (index0)
# │    sub_arr=[1], tracker=[True, False, False]
# │    ├── pick nums[0]=1 → tracker[0]=True → skip
# │    ├── pick nums[1]=1
# │    │     sub_arr=[1,1], tracker=[True, True, False]
# │    │     ├── pick nums[0]=1 → tracker[0]=True → skip
# │    │     ├── pick nums[1]=1 → tracker[1]=True → skip
# │    │     └── pick nums[2]=2
# │    │           sub_arr=[1,1,2], tracker=[True, True, True] → append [1,1,2]
# │    │           backtrack → sub_arr=[1,1], tracker=[True, True, False]
# │    │
# │    └── pick nums[2]=2
# │          sub_arr=[1,2], tracker=[True, False, True]
# │          ├── pick nums[0]=1 → tracker[0]=True → skip
# │          ├── pick nums[1]=1
# │          │     sub_arr=[1,2,1], tracker=[True, True, True] → append [1,2,1]
# │          │     backtrack → sub_arr=[1,2], tracker=[True, False, True]
# │          └── pick nums[2]=2 → tracker[2]=True → skip
# │
# ├── pick nums[1]=1
# │    sub_arr=[], tracker=[False, False, False]
# │    ⚡ Condition: nums[1]==nums[0] and tracker[0]==False → continue executes here
# │    branch skipped
# │
# └── pick nums[2]=2 (index2)
#      sub_arr=[2], tracker=[False, False, True]
#      ├── pick nums[0]=1
#      │     sub_arr=[2,1], tracker=[True, False, True]
#      │     └── pick nums[0]=1 → tracker[0]=True → skip
#      │     └── pick nums[1]=1
#      │           sub_arr=[2,1,1], tracker=[True, True, True] → append [2,1,1]
#      │           backtrack → sub_arr=[2,1], tracker=[True, False, True]
#      │     └── pick nums[2]=2 → tracker[2]=True → skip
#      ├── pick nums[1]=1
#      │    ⚡ Condition: nums[1]==nums[0] and tracker[0]==False → continue executes here
#      └── pick nums[2]=2 → tracker[2]=True → skip
