import sys

[n] = [int(x) for x in sys.stdin.readline().split()]
A = [int(x) for x in sys.stdin.readline().split()]

def sum(A, n):
    res = 0
    for i in range(0, n):
        res += A[i]
    return res

print(sum(A, n))