from collections import deque

edges = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]
V = 6

def topological_sort(V,adj):
    indegree_arr = [0]*V
    for inner_arr in adj:
        for item in inner_arr:
            indegree_arr[item] = indegree_arr[item]+1

    queue  = deque()
    visited = set()
    for index, item in enumerate(indegree_arr):
        if item == 0:
            queue.append(index)
            visited.add(index)

    ans = []
    while queue.__len__() != 0:
        item = queue.popleft()
        ans.append(item)

        for inner_item in adj[item]:
            indegree_arr[inner_item] = indegree_arr[inner_item] - 1

            if inner_item not in visited and indegree_arr[inner_item]==0:
                visited.add(inner_item)
                queue.append(inner_item)
    return ans


def edge_to_adj(V,edges):
    adj = [[] for _ in range(V)]
    for e1,e2 in edges:
        adj[e1].append(e2)
    return adj


adj = edge_to_adj(V,edges)
print(topological_sort(V,adj))
