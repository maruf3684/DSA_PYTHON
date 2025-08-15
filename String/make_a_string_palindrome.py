s = "leetcode"
#ans : leetcodocteel

s= "cvwiievjz"

def make_palindrome_brutforce_wrong(s):
    i = 0
    main_len = len(s)
    j = main_len -1
    while i<j:
        if s[i] != s[j]:
            prev = s[:j]
            curr = s[j]
            next = s[j+1:]
            new_add = s[i]
            s = prev + curr + new_add + next
            i+=1
        else:
            i+=1
            j-=1
    return len(s)-main_len

print(make_palindrome_brutforce_wrong(s))



def make_palindrome_dp_solution(s,left,right,memo):
    if left >= right:
        return 0
    if (left, right) in memo:
        return memo[(left, right)]
    if s[left] == s[right]:
        return make_palindrome_dp_solution(s,left+1,right-1,memo)
    else:
        memo[(left, right)] =  1 + min(
            make_palindrome_dp_solution(s,left+1,right,memo),
            make_palindrome_dp_solution(s,left,right-1,memo)
        )
        return memo[(left, right)]

print(make_palindrome_dp_solution("cvwiievjz",0,s.__len__()-1,{}))



def make_palindrome_kmp(s):
    pass


#print(make_palindrome_kmp(s))




#Edge cases
# if s == "zjveiiwvc":
#     return 5
# if s == "ccewnxhytsr":
#     return 9
# if s == "swizunxvbbvjr":
#     return 9



#for qs : zjveiiwvc
# My ans: 8
# # zjveiiwvc|vwiievjz

#for qs : zjveiiwvc
# Actual ans: zjcvewiiwevcjz
# Minimum insertions needed: 5
# Inserted chars & spots (relative to the result):
# 	•	Insert c at position 2 → zj[c]...
# 	•	Insert w at position 5 → zjcve[w]...
# 	•	Insert e at position 9 → ...wiiw[e]...
# 	•	Insert j at position 12 → ...evc[j]...
# 	•	Insert z at position 13 → ...cj[z]