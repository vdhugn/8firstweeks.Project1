import sys

[n, m] = [int(x) for x in sys.stdin.readline().split()]
A = [int(y) for y in sys.stdin.readline().split()]

def countPairs(A, m, n):
  count = 0
  seen = set()
  for j in range(n):
    if m - A[j] in seen:
      count += 1
    else:
      seen.add(A[j])
  return count

print(countPairs(A, m, n))
