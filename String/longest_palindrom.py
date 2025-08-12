s = "abccccdd"
#s = "ccc"


def longestPalindrom(s):
    tracker = {}
    ans = 0
    flag_odd = True
    for i in s:
        tracker[i] = tracker.get(i,0)+1

    if len(tracker) == 1:
        return len(s)

    for i in tracker:
        if tracker[i] % 2 == 0:
            ans += tracker[i]
        else:
            if flag_odd:
                ans += 1
                flag_odd = False
            ans += tracker[i]-1
    return ans

print(longestPalindrom(s))

