from collections import defaultdict



#sorting approach
def group_anagram(strs):
    ans_dict = {}
    for st in strs:
        int_value = ''.join(sorted(st))
        ans_dict.setdefault(int_value, []).append(st)
    return list(ans_dict.values())


#counting approach
# tracker dict look like this:
# {
#   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]=[eat, tea, ate],
#   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]=[tan, nat],
#   [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]=[bat]
# }
def group_anagram2(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    print(res)
    return list(res.values())





print(group_anagram2(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
