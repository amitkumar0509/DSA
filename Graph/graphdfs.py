# by stack method 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []

}
def dfs(graph,source):
    stack = []
    stack.append(source)
    while stack:
        node = stack.pop()
        print(node)
        for neighbour in graph[node]:
            stack.append(neighbour)
dfs(graph,'A')