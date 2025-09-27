from collections import deque

adj = [
    [2, 3, 1],
    [0],
    [0, 4],
    [0],
    [2]
]

#Output: [0, 2, 3, 1, 4]

adj = [
    [10],
    [1, 2 ,4, 8],
    [0 ,5, 6, 9],
    [0 ,4],
    [7 ,8],
    [0, 2],
    [1, 8],
    [1, 7, 9],
    [3, 6],
    [0, 3, 5],
    [1, 6],
]

def bfs(adj):
    queue = deque()
    ans = []
    tracker = {0}
    queue.append(0)

    while queue.__len__() != 0:
        item = queue.popleft()
        ans.append(item)
        for neibour in adj[item]:
            if neibour not in tracker:
                tracker.add(neibour)
                queue.append(neibour)
    return ans



print(bfs(adj))