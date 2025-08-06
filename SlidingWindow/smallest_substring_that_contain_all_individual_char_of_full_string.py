

s = "ADOBECODEBANC"
t = "ABC"

# s = "A"
# t = "AA"
#
# s = "A"
# t = "B"
#
# s = "AC"
# t = "AB"
#
# s = "A"
# t = "A"





def find_substring(s,t):
    fast,slow,total= 0,0,0
    frequency,tracker = {},{}
    ans =  None
    lenght = float('inf')

    for i in t:
        frequency[i] = frequency.get(i,0)+1
        total += 1

    while fast < len(s):
        tracker[s[fast]] = tracker.get(s[fast],0)+1
        if s[fast] in frequency:
            if tracker[s[fast]] <= frequency[s[fast]]:
                total -= 1

        while total == 0:
            if fast-slow+1 < lenght:
                ans = [slow,fast]
                lenght = fast-slow+1

            tracker[s[slow]] = tracker.get(s[slow],0)-1
            if s[slow] in frequency:
                if tracker[s[slow]] < frequency[s[slow]]:
                    total += 1
            slow += 1
        fast+=1

    return s[ans[0]:ans[1] + 1] if ans else ""

print(find_substring(s,t))
