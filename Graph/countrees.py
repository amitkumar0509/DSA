def count_trees_in_forest(n,edges):
    adj = {i: [] for i in range(n)}
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                dfs(neighbor)
    count = 0
    for i in range(n):
        if i not in visited:
            dfs(i)
            count += 1  
    return count
# Example usage:
n = 7
edges = [[0, 1], [1, 2], [3, 4]]
print(count_trees_in_forest(n, edges))  # Output: 2