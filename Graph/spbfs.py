from collections import deque
def shortest_path(graph, start, end):
    visited = set()
    queue = deque([(start, [start])])
    visited.add(start)
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(shortest_path(graph, 'A', 'F'))  # Output: ['A',