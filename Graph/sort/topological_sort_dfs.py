from collections import deque
edges = [
    [3, 0],
    [1, 0],
    [2, 0]
]
V = 4

edge = [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5,2]]
V = 6



def dfs(edges,tracker_array,stack,node):
    tracker_array[node] = True
    for item in edges[node]:
        if not tracker_array[item]:
            dfs(edges,tracker_array,stack,item)
    stack.append(node)


def topological_sort(V,edges):
    stack = deque()
    tracker_array = [False]*V
    for i in range(0,len(tracker_array)):
        item = i
        if not tracker_array[item]:
            dfs(edges,tracker_array,stack,item)
    return list(reversed(stack))


def edge_to_adjancy(edges,V):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    return adj




edges = edge_to_adjancy(edges,V)
print(topological_sort(V,edges))






#Topological sort is a linear ordering of a Directed Acyclic Graph’s vertices such that for every edge u → v, u appears before v.
#ex : 4->5->1->2->3 ans: 3,2,1,5,4  ->  4,5,1,2,3