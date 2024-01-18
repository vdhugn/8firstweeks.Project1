n = int(input())

def permutation(n):
  permutations = []
  current_permutation = [0] * n

  def permutation_recursive(k):
    if k == n:
      permutations.append(' '.join(map(str, current_permutation[:])) + ' ')
      return

    for i in range(1, n + 1):
      if i not in current_permutation[:k]:
        current_permutation[k] = i
        permutation_recursive(k + 1)

  permutation_recursive(0)
  return permutations

res = permutation(n)

for permutation in res:
  print(permutation)

