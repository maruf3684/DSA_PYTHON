def longest_common_prefix(strs):
    shortest_str = strs[0]
    for st in strs:
        if st.__len__()<shortest_str.__len__():
            shortest_str = st

    ans = ""
    for i in range(0,len(shortest_str)):
        target = shortest_str[i]
        break_flag =  False
        for index,item in enumerate(strs):
            if item[i] != target:
                break_flag = True
                break
        if break_flag:
            break
        else:
            ans = ans + shortest_str[i]
    return ans


print(longest_common_prefix(["flower","flow","flight"]))
