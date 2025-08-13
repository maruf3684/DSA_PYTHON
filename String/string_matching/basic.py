parent = "abcdefg"
chield = "def"


def string_matching(parent, chield):
    parent_ptr = 0
    parent_pointer_tracker = 0
    chield_ptr = 0

    while parent_ptr < len(parent):
        if parent[parent_ptr] == chield[chield_ptr]:
            parent_ptr += 1
            chield_ptr += 1
            if chield_ptr == len(chield):
               return parent_pointer_tracker
        else:
            if chield_ptr == 0:
                parent_ptr+=1
                parent_pointer_tracker+=1
            else:
                parent_pointer_tracker+=1
                parent_ptr = parent_pointer_tracker
                chield_ptr = 0
    return -1

print(string_matching(parent, chield))




