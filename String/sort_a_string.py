s = "lkjhgfdsaarrtt"


def sort_string(s):
    ans = []
    track = {}
    for i in s:
        track[i] = track.get(i, 0) + 1

    for i in range(97,123):
        if chr(i) in track:
            word = chr(i) * track.get(chr(i))
            ans.append(word)
    return "".join(ans)

print(sort_string(s))

