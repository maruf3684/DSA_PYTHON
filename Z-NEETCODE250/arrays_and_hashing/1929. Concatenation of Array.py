
# def getConcatenation(nums):
#     ans = [0]*(2*len(nums))
#
#     for i in range(0,len(ans)):
#         iterator = i
#         if iterator > len(nums)-1:
#             iterator = iterator - len(nums)
#         ans[i] = nums[iterator]
#     return ans

def getConcatenation(nums):
    return nums+nums

print(
    getConcatenation([1,2,3,4])
)
