import sys
def input():
    [n, m]=[int(x) for x in sys.stdin.readline().split()]
    A=[]
    for i in range(m):
        [u, v]=[int(x) for x in sys.stdin.readline().split()]
        A.append([u, v])
    return n,m,A

def dfs(graph,node,visited=set()):
    print(node, end = ' ')
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(graph,child,visited)

n, m, A = input()
graph={}

for i in range(1,n+1):
    graph[i]=[]
for u,v in A:
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
dfs(graph,1)

