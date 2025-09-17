
n = 4
k = 2
#Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]


def combination(n, k, sub_array,ans):
    if n == 0:
        if sub_array.__len__() == k:
            ans.append(sub_array)
    else:
        pick = [*sub_array, n]
        non_pick = [*sub_array]

        combination(n - 1, k, pick,ans)
        combination(n - 1, k, non_pick,ans)
    return ans




def combination_back_trac(n, k, sub_array, ans):
    if len(sub_array) == k:
        ans.append(sub_array[:])
        return
    if n == 0:
        return

    sub_array.append(n)
    combination(n-1, k, sub_array, ans)
    sub_array.pop()
    combination(n-1, k, sub_array, ans)




def combination_back_trac_with_return(n, k, sub_array):
    if len(sub_array) == k:
        return [sub_array[:]]
    if n == 0:
        return []

    sub_array.append(n)
    pick = combination_back_trac_with_return(n-1, k, sub_array)
    sub_array.pop()
    non_pick = combination_back_trac_with_return(n-1, k, sub_array)

    return pick + non_pick





print(combination(n, k, [],[]))