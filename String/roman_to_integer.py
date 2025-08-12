s = "MCMXCIV"

def romanToInt(s):
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    ans = []
    for i in range(len(s)):
        if i == len(s)-1:
            ans.append(roman[s[i]])
            break
        if roman.get(s[i]) < roman.get(s[i+1]):
            ans.append(-roman[s[i]])
        else:
            ans.append(roman[s[i]])

    return sum(ans)



print(romanToInt(s))
