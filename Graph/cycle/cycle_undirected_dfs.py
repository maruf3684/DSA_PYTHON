edges = [[0, 1], [0, 2], [1, 2], [2, 3]]
V = 4


# V = 4
# edges= [[0, 1], [1, 2], [2, 3]]

# edges = [[2],[1],[0,1]]
# V = 3

def edges_to_adj(edges,V):
    adj = [[] for _ in range(V)]
    for fr,to in edges:
        adj[fr].append(to)
        adj[to].append(fr)
    return adj



def detect_cycle(adj, current, parent, visited):
    visited.add(current)
    for naibour in adj[current]:
        if naibour not in visited:
            if detect_cycle(adj, naibour, current, visited):
                return True
        elif naibour != parent:
            return True
    return False


adj = edges_to_adj(edges, V)
visited = set()
for v in range(V):
    if v not in visited:
        if detect_cycle(adj, v, -1, visited):
            print(True)
        else:
            print(False)


## main trick line: Visited neibur parent noy

#         1
#         .
#         5
#       .   .
#     6.......7