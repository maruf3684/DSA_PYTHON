
sentence = "thequickbrownfoxjumpsoverthelazydog"


def panagram(sentence):
    tracker = {}
    for char in sentence:
        tracker[char] = tracker.get(char,0) + 1

    for i in range(97,123):
        if chr(i) not in tracker:
            return False
    return True

print(panagram(sentence))