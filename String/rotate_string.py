s = "abcde"
goal = "cdeab"

def rotate_string(s, goal):
    if s == goal:
        return True
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        if s[i:] + s[:i] == goal:
            return True
    return False


ans = rotate_string(s, goal)
print(ans)