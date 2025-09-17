# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.


s = "abca"


def check_valid_palindrom(s,l,r,chance = 1):
    if l==r or l>r:
        return True
    if s[l] == s[r]:
        result = check_valid_palindrom(s,l+1,r-1,chance)
        return result
    else:
        if chance == 0:
            return False
        result_skip_left = check_valid_palindrom(s, l + 1, r,chance-1)
        result_skip_right = check_valid_palindrom(s, l , r - 1,chance-1)

        return result_skip_left or result_skip_right




print(check_valid_palindrom(s,0,s.__len__()-1))