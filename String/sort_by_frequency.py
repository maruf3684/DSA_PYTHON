from collections import Counter, defaultdict

s = "tree"


def sort_by_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    bucket = {}
    most_freq = float('-inf')

    for key, value in freq.items():
        bucket.setdefault(value, []).append(key * value)
        most_freq = max(most_freq, value)

    ans = []
    for i in range(most_freq, -1, -1):
        if i in bucket:
            ans.extend(bucket[i])

    return "".join(ans)

print(sort_by_frequency(s))

