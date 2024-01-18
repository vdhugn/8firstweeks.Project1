from collections import deque

def max_flow(graph, source, target):
    residual_graph = [[0] * len(graph) for _ in range(len(graph))]
    parent = [-1] * len(graph)

    max_flow_value = 0

    while True:
        # Find augmenting path using BFS
        if not bfs(graph, residual_graph, source, target, parent):
            break

        # Find the minimum capacity along the augmenting path
        path_flow = float('inf')
        s = target
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        # Update residual capacities of the edges and reverse edges
        v = target
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

        max_flow_value += path_flow

    return max_flow_value

def bfs(graph, residual_graph, source, target, parent):
    visited = [False] * len(graph)
    queue = deque()

    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()

        for v, capacity in enumerate(graph[u]):
            if not visited[v] and residual_graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u

                if v == target:
                    return True

    return False

# Input processing
N, M = map(int, input().split())
graph = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u-1][v-1] += 1  # Assuming capacity of each edge is 1

s, t = map(int, input().split())

# Output the max flow value
print(max_flow(graph, s-1, t-1))
