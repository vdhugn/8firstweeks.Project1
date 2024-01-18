n = int(input())
def fibonacci(n):
  if n < 0:
    raise ValueError("n must be a non-negative integer")
  elif n == 0 or n == 1:
    return n
  else:
    a = 0
    b = 1
    for i in range(2, n + 1):
      c = a + b
      a = b
      b = c
    return c
print(fibonacci(n-1))