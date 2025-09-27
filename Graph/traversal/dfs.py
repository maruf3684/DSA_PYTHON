adj = [
    [2, 3, 1],
    [0],
    [0, 4],
    [0],
    [2]
]


def dfs(adj,start,ans,tracker):
    ans.append(start)
    tracker.add(start)
    for item in adj[start]:
        if item not in tracker:
            dfs(adj,item,ans,tracker)
    return ans


print(dfs(adj,0,[],{0}))