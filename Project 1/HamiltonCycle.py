from collections import defaultdict

def isHamilton(graph, path, visited):
    if len(path) == len(graph):
        if path[-1] in graph[path[0]]:
            return True
        return False
    
    current = path[-1]
    for neighbor in graph[current]:
        if neighbor not in path and not visited[neighbor]:
            path.append(neighbor)
            visited[neighbor] = True
            if isHamilton(graph, path, visited):
                return True
            path.pop()
            visited[neighbor] = False

    return False

def check_hamiltonian(graph):
    for node in graph:
        visited = {node: False for node in graph}
        path = [node]
        visited[node] = True
        if isHamilton(graph, path, visited):
            return 1
    return 0

line= int(input())
results = []

for _ in range(line):
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    result = check_hamiltonian(graph)
    results.append(result)

for result in results:
    print(result)