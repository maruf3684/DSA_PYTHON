def isAnagram(s, t):
    tracker = {}
    tracker2 = {}
    for index,item in enumerate(t):
        tracker[item] = tracker.get(item,0)+1
    for index, item in enumerate(s):
        tracker2[item] = tracker2.get(item,0)+1

    return tracker2 == tracker



print(isAnagram(s = "anagram", t = "nagaram"))