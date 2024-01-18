n = int(input())

def list_seq(n):
    L=[]
    for i in range(100, 1000):
        if i % n == 0:
            L.append(str(i))
    res = " ".join(L)
    return res

print(list_seq(n))
