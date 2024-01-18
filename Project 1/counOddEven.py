import sys

[n] = [int(x) for x in sys.stdin.readline().split()]
A = [int(x) for x in sys.stdin.readline().split()]

odd = 0
even = 0
for i in range(n):
    if A[i] % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd, even)