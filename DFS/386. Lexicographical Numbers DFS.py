
def lexicographic(n):
    ans = []
    for i in range(1,10):
        dfs(ans,i,n)
    return ans


def dfs(ans,i,n):
    if i>n:
        return
    ans.append(i)
    for j in range(10):
        next_num = i*10+j
        if next_num>n:
            break
        dfs(ans,next_num,n)





print(lexicographic(13))