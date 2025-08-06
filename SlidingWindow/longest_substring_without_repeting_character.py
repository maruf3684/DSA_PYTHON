
s = "pwwkew"

def find_max_length(s):
    fast = 0
    slow = 0
    tracker = {}
    final_length = 0

    while fast < len(s):
        if s[fast] not in tracker or tracker[s[fast]] < 1:
            tracker[s[fast]] = 1
            final_length = max(final_length,fast-slow+1)
            fast+=1
        else:
            while s[slow] != s[fast]:
                tracker[s[slow]]-=1
                slow += 1
            tracker[s[slow]] -= 1
            slow += 1
            tracker[s[fast]]+=1
            fast+=1
    return final_length

print(find_max_length(s))