s = "leetcode"
s = "aaa"

def make_palindrome_kmp(s):
    new_s = s + "#" +  s[::-1]
    print(new_s)
    lps = [0] * len(new_s)
    start = 0
    end = 1
    while end < len(new_s):
        if new_s[start] == new_s[end]:
            lps[end] = start+1
            start+=1
            end+=1
        else:
            if start > 0:
                # 0 er processing o upper if block a hobe
                prefix_part_non_match_point = lps[start-1]
                start = prefix_part_non_match_point
            else:
                lps[end] = 0
                end+=1
    print(lps)
    caracter_need_to_add = len(s) - lps[-1]
    return caracter_need_to_add

print(make_palindrome_kmp(s))


# leetcode | edocteel

# teetcode teetedoc
# 01230000 45670000