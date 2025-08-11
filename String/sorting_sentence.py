s = "Myself2 Me1 I4 and3"

#s = "is2 sentence4 This1 a3"

def sortSentence(s):
    string_arr = s.split()
    result = [""]*len(string_arr)
    for selected_word in string_arr:
        for i ,ch in enumerate(selected_word):
            if ch.isdigit():
                word = selected_word[:i]
                digit = int(selected_word[i:])
                result[digit-1] = word
    return " ".join(result)


print(sortSentence(s))












sortSentence(s)