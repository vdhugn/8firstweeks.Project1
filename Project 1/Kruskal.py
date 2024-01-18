import sys
def input():
    [n, m]=[int(x) for x in sys.stdin.readline().split()]
    E=[]
    for i in range(m):
        [u,v,w]=[int(x) for x in sys.stdin.readline().split()]
        E.append([u, v, w])
    return n,m,E

n,m,E=input()
E=sorted(E, key=lambda x: x[2])
#print(E)

#Data Structure for disjoint set
p=[0 for i in range(n+1)]
r=[0 for i in range(n+1)]

def FindSet(x):
    if x != p[x]:
        p[x]=FindSet(p[x])
    return p[x]

def Unify(x, y):
    if r[x]>r[y]:
        p[y]=x #make y the child of x
    else:
        p[x]=y #make x the child of y
        if r[x]==r[y]:
            r[y]=r[y]+1

def MakeSet(x):
    p[x]=x
    r[x]=0

def PrintDisjointSet():
    for i in range(n+1):
        print('p[',i,']=',p[i],' r[',i,']=',r[i])

def Kruskal():
    for v in range(1, n+1):
        MakeSet(v)
    T=[]
    for [u, v, w] in E:
        ru=FindSet(u) #the root of tree containing u
        rv=FindSet(v) #the root of tree containing v
        if ru != rv:
            #accept to insert the edge (u,v) to the solution (spanning tree under contructor)
            Unify(ru, rv)
            T.append([u, v, w])
            if len(T)==n-1:
                break
    return T #the list of selected edges odd the mst of g

MST=Kruskal()
res = 0
for i in range(len(MST)):
    res += MST[i][2]
print(res)