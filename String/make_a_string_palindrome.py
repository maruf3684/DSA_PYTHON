s = "leetcode"
#ans : leetcodocteel

def make_palindrome_brutforce(s):
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

print(make_palindrome_brutforce(s))










