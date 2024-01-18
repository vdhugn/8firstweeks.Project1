import sys

n = int(input())
A = [int(x) for x in sys.stdin.readline().split()]

def check(A, n):
  res = [0] * n
  seen = set()
  for i in range(n):
    if A[i] in seen:
      res[i] = 1
    else:
      seen.add(A[i])
  return res

result_list = check(A, n)
for i in range(len(result_list)):
  print(result_list[i])