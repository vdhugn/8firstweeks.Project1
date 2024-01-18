#PYTHON 
def bfs(graph, start_node):
  visited = set()
  queue = [start_node]

  while queue:
    node = queue.pop(0)
    visited.add(node)

    for adjacent_node in graph[node]:
      if adjacent_node not in visited:
        queue.append(adjacent_node)

  return sorted(visited)

def main():
  n, m = map(int, input().split())
  graph = {}

  for i in range(1, n + 1):
    graph[i] = []

  for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

  start_node = 1
  visited = bfs(graph, start_node)
  print(' '.join(map(str, visited)))

if __name__ == '__main__':
  main()