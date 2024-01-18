import sys
[k, n]=[int(x) for x in sys.stdin.readline().split()]

def C(k, n):
  if k < 0 or n < 0 or k > n:
    raise ValueError("Invalid arguments.")

  if k == 0 or k == n:
    return 1

  dp = [0] * (n + 1)
  dp[0] = 1
  dp[1] = 1

  for i in range(2, n + 1):
    for j in range(min(i, k) + 1, 0, -1):
      dp[j] = dp[j] + dp[j - 1]

  return dp[k]

print(C(k, n))