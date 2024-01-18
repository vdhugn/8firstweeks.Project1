import sys
import numpy as np
class PriorityQueue:
    def __init__(self,max_size):
        self.sz = max_size # element of priority queue
        self.n = 0 # size of heap
        self.keys = [0 for i in range(self.sz + 1)]
        self.nodes = [0 for i in range(self.sz + 1)]
        self.idx = [-1 for i in range(self.sz + 1)]

    def Swap(self,i,j):
        tmp = self.nodes[i]
        self.nodes[i] = self.nodes[j]
        self.nodes[j] = tmp
        self.idx[self.nodes[i]] = i
        self.idx[self.nodes[j]] = j

    def Size(self):
        return self.n

    def UpHeap(self,i):
        if i==0:
            return
        while i>0:
            pi = (i-1)//2 # parent of i
            if self.keys[self.nodes[i]] < self.keys[self.nodes[pi]]:
                self.Swap(i,pi)
            else:
                break
            i = pi
    
    def DownHeap(self,i):
        L = 2*i + 1 # index of the left-child
        R = 2*i + 2 # index of the right-child
        minIdx = i
        if L < self.n and self.keys[self.nodes[L]] < self.keys[self.nodes[minIdx]]:
            minIdx = L
        if R < self.n and self.keys[self.nodes[R]] < self.keys[self.nodes[minIdx]]:
            minIdx = R
        if minIdx != i:
            self.Swap(i, minIdx)
            self.DownHeap(minIdx)
    
    def Insert(self,v,k):
        self.keys[v] = k
        self.nodes[self.n] = v
        self.idx[self.nodes[self.n]] = self.n
        self.UpHeap(self.n)
        self.n = self.n + 1

    def InHeap(self,v):
        return self.idx[v] >= 0
    
    def UpdateKey(self,v,k):
        if self.keys[v] > k:
            self.keys[v] = k
            self.UpHeap(self.idx[v])
        else:
            self.keys[v] = k
            self.DownHeap(self.idx[v])

    def DeleteMin(self):
        sel_node = self.nodes[0]
        self.Swap(0,self.n-1)
        self.n = self.n - 1
        self.DownHeap(0)
        self.idx[sel_node] = -1
        return sel_node
    
    def GetKey(self,v):
        return self.keys[v]

    def Print(self):
        for i in range(self.n):
            e = self.nodes[i]
            print('[',e,'idx',self.idx[e],',k',self.keys[e],',',end='')
        print('')

def Input():
    [n,m] = [int(x) for x in sys.stdin.readline().split()]
    A = [[] for i in range(n+1)]
    for i in range(m):
        [u,v,w] = [int(x) for x in sys.stdin.readline().split()]
        A[u].append([v,w])
    return n,m,A

def DijkstraPriorityQueue(n,m,A,s,t):
    pq = PriorityQueue(n)
    pq.Insert(s,0)
    while pq.Size() > 0:
        u = pq.DeleteMin()
        if u == t:
            break
        du = pq.GetKey(u)
        for [v,w] in A[u]:
            dv = du + w
            if pq.InHeap(v) == False:
                pq.Insert(v,dv)
            else: 
                if pq.GetKey(v) > dv:
                    pq.UpdateKey(v,dv)
    return (pq.GetKey(t))

n,m,A = Input()
list1 = []
for s in range(1, n+1):
    for t in range(1, n+1):
        list1.append(DijkstraPriorityQueue(n,m,A,s,t))

matrix = np.array(list1).reshape((n, n))
for i in range(n):
    print(' '.join(map(str, matrix[i])))