s = ['A','B','C','A','B','D','A','B','C','A','B','C','A','B','D']
k = [ 0,  0,  0,  1,  2,  0,  1,  2,  3,  4,  5,  3,  4,  5,  6]


s = "abcabdabcabcabd"

def kmp_algo(s):
    prefix_pointer = 0
    suffix_pointer = 1
    match_length_tracker_array = [0]

    while suffix_pointer < len(s):
        if s[prefix_pointer] == s[suffix_pointer]:
            match_length_tracker_array.append(prefix_pointer+1)
            suffix_pointer += 1
            prefix_pointer += 1
        else:
            if prefix_pointer > 0:
                prefix_pointer = match_length_tracker_array[prefix_pointer-1]
            else:
                match_length_tracker_array.append(0)
                suffix_pointer += 1
    print(match_length_tracker_array)
    return s[:match_length_tracker_array[-1]]

print(kmp_algo(s))
