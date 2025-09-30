edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
V = 4

# Akta node 2 bar visit hole cycle ache. parent bade visit korte hobe




from collections import deque

def edge_to_adj(edge,V):
    adj = [[] for _ in range(V)]
    for i,j in edge:
        adj[i].append(j)
        adj[j].append(i)
    return adj


def bfs(start, adj, visited):
    queue = deque()
    queue.append((start, -1))
    visited[start] = True

    while queue:
        node, parent = queue.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, node))
            elif neighbor != parent:
                return True
    return False


def solve(edges, V):
    adj = edge_to_adj(edges, V)
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            if bfs(i, adj, visited):
                return True
    return False

ans = solve(edges,V)
print(ans)