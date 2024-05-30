
def odd_vertices(n, edges):
    deg = [0] * n
    for (a,b) in edges:
        deg[a] += 1
        deg[b] += 1
    return [a for a in range(n) if deg[a] % 2]

def is_edge_connected(n, edges):
    if n == 0 or len(edges) == 0:
        return True
    succ = [[] for a in range(n)]
    for (a,b) in edges:
        succ[a].append(b)
        succ[b].append(a)
    touched = [False] * n
    init = edges[0][0]
    touched[init] = True
    todo = [init]
    while todo:
        s = todo.pop()
        for d in succ[s]:
            if touched[d]:
                continue
            touched[d] = True
            todo.append(d)
    for a in range(n):
        if succ[a] and not touched[a]:
            return False
    return True

def is_eulerian(n, edges):
    return is_edge_connected(n, edges) and not odd_vertices(n, edges)

# à Faire
def find_eulerian_path: