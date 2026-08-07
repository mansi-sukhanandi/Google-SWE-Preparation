def dfs(node, graph, visited):
    if node in visited:
        return
        
    visited.add(node)
    print("Visited:", node)
    
    # Har neighbor address/node par DFS
    for neighbor in graph[node]:
        dfs(neighbor, graph, visited)
