# s = "onions"
# s2 = "onionionson"

s = "a"
s2 = "a"


def get_kmp_of_first_string(s):
    if s.__len__() ==  1:
        return [1]
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
    return match_length_tracker_array

def find_substring(s, s2):
    kmp_of_first_string = get_kmp_of_first_string(s)
    first = 0
    second = 0

    while second < len(s2):
        if s[first] == s2[second]:
            first += 1
            second += 1
        else:
            if first > 0:
                first = kmp_of_first_string[first-1]
            else:
                second += 1

        if first == len(s):
            return second - len(s)

    return -1



print(find_substring(s, s2))