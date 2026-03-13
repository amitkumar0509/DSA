graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []

}
def bfs(graph,source):
    queue = []
    queue.append(source)
    while queue:
        node = queue.pop(0)
        print(node)
        for neighbour in graph[node]:
            queue.append(neighbour)
bfs(graph,'A')