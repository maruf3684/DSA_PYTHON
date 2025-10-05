
def lexicographic(n):
    ans = []
    for i in range(1,n+1):
        ans.append(str(i))

    for index , item in enumerate(sorted(ans)):
        ans[index] = int(item)

    return ans





print(lexicographic(1500))