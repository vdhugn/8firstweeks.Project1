import sys

def Input():
    [n, m] = [int(x) for x in sys.stdin.readline().split()]

    graph = {}
    for i in range(m):
        u, v, w = [int(x) for x in sys.stdin.readline().split()]
        if u not in graph:
            graph[u] = {}
            graph[u][v] = int(w)
        else:
            graph[u][v] = int(w)

    [start, end] = [int(x) for x in sys.stdin.readline().split()]
    return n, m, graph, start, end

def dijkstra(graph, start, end):
    distances = {}
    predecessor = {}

    for node in graph:
        distances[node] = sys.maxsize
        predecessor[node] = None

    distances[start] = 0
    unvisited = set(graph.keys())

    while unvisited:
        current = None
        min_distance = sys.maxsize
        for node in unvisited:
            if distances[node] < min_distance:
                current = node
                min_distance = distances[node]

        if current == end:
            break
    
        unvisited.remove(current)
        for neighbor, weight in graph[current].items():
            distance = distances[current] + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessor[neighbor] = current

    # path = []
    # current = end
    # while current is not None:
    #     path.append(current)
    #     current = predecessor[current]

    # path = path[::-1]

    return distances[end]

n, m, graph, start, end = Input()
shortest_path = dijkstra(graph, start, end)
print(shortest_path)