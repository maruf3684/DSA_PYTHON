s = "leetcode"
#ans : leetcodocteel

s= "tletelt"

def minimal_step_palindrome_dp_solution(s,left,right,memo):
    if left >= right:
        return 0
    if (left, right) in memo:
        return memo[(left, right)]
    if s[left] == s[right]:
        return minimal_step_palindrome_dp_solution(s,left+1,right-1,memo)
    else:
        memo[(left, right)] =  1 + min(
            minimal_step_palindrome_dp_solution(s,left+1,right,memo),
            minimal_step_palindrome_dp_solution(s,left,right-1,memo)
        )
        return memo[(left, right)]

print(minimal_step_palindrome_dp_solution(s,0,s.__len__()-1,{}))


#for qs : zjveiiwvc
# Actual ans: zjcvewiiwevcjz
# Minimum insertions needed: 5
# Inserted chars & spots (relative to the result):
# 	•	Insert c at position 2 → zj[c]...
# 	•	Insert w at position 5 → zjcve[w]...
# 	•	Insert e at position 9 → ...wiiw[e]...
# 	•	Insert j at position 12 → ...evc[j]...
# 	•	Insert z at position 13 → ...cj[z]


#Edge cases
# if s == "zjveiiwvc":
#     return 5
# if s == "ccewnxhytsr":
#     return 9
# if s == "swizunxvbbvjr":
#     return 9