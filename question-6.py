def dfs(graph, node, visited, record):
    visited.add(node)
    record.add(node)
    for neigbhor in graph.get(node,[]):
        if neigbhor not in visited:
            if dfs(graph, neigbhor,visited,record):
                return True
        if neigbhor in record:
            return True
    record.remove(node)
    return False
def detect_cycle(graph):
    visited = set()
    record = set()
    for i in graph:
        if i not in visited and  dfs(graph,i,visited,record):
            return True
    return False
graph = {
    0: [1],
    1: [2],
    2: [3],
    3: [0]
}
print(detect_cycle(graph))


