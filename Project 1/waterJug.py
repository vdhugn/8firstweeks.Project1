import sys
[a, b, c] = [int(x) for x in sys.stdin.readline().split()]


class State:
    def __init__(self, x, y, step):
        self.x = x #amount of water in jug 1
        self.y = y #amount of water in jug 2
        self.step = step #number of step 

def finalState(s):
    return s.x == c or s.y == c

def solve():
    Q = [] #initialize an empty queue
    visited=[[False for i in range(1000)] for i in range(1000)]
    s0 = State(0, 0, 0)
    Q.append(s0) #push the initial state into the queue Q
    visited[0][0] = True
    while len(Q) > 0:
        s = Q.pop(0) #pop an element out of the queue (in the fron, index)
        
        #Fill Jug 1
        ns = State(a, s.y, s.step + 1) 
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
        
        #Fill Jug 2
        ns = State(s.x, b, s.step + 1) 
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True

        #Empty Jug 1
        if s.x > 0:
            ns=State(0, s.y, s.step + 1)
            if finalState(ns):
                return ns
            if visited[ns.x][ns.y] == False:
                Q.append(ns)
                visited[ns.x][ns.y] = True

        #Empty Jug 2
        if s.y > 0:
            ns=State(s.x, 0, s.step + 1)
            if finalState(ns):
                return ns
            if visited[ns.x][ns.y] == False:
                Q.append(ns)
                visited[ns.x][ns.y] = True

        #Pour Jug 1 to Jug 2
        if s.x + s.y <= b and s.y < b:
            ns=State(0, s.x + s.y, s.step + 1)
        else:
            ns=State(s.x + s.y - b, b, s.step + 1)
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True

        #Pour Jug 2 to Jug 1
        if s.x + s.y <= a and s.x < a:
            ns=State(s.x + s.y, 0, s.step + 1)
        else:
            ns=State(a, s.x + s.y - a, s.step + 1)
        if finalState(ns):
            return ns
        if visited[ns.x][ns.y] == False:
            Q.append(ns)
            visited[ns.x][ns.y] = True
    
    return None #no solution found

res=solve()
if res==None:
    print(-1)
else:
    print(res.step)
    s=res
    stack=[]

    while len(stack)>0:
        s=stack.pop()
        print(s.action, '(',s.x,',',s.y,')')