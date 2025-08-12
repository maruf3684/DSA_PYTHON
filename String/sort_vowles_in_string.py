s = "lEetcOde"

#"lEOtcede"


def sort_vowels(s):
    vowels = {'A':0,'E':0,'I':0,'O':0,'U':0,'a':0,'e':0,'i':0,'o':0,'u':0}
    freq = {}
    for i in s:
        if i in vowels:
            freq[i] = freq.get(i,0) + 1
    new_s = []
    for keys,value in vowels.items():
        if keys in freq:
            new_s.extend(keys * freq[keys])

    main_string = list(s)
    new_s_pointer = 0
    for i in range(len(main_string)):
        if main_string[i] in vowels:
            main_string[i] = new_s[new_s_pointer]
            new_s_pointer += 1
    return "".join(main_string)


print(sort_vowels(s))

