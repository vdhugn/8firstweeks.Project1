import sys

def count_even_weight_subsequences(k, m):
  table = [[0 for _ in range(k + 1)] for _ in range(m + 1)]

  for i in range(m + 1):
    table[i][0] = 1

  for i in range(1, m + 1):
    for j in range(1, k + 1):
      # If the current element is even, then we can either include it in the subsequence or not.
      if i % 2 == 0:
        table[i][j] = table[i - 1][j] + table[i - 1][j - 1]
      # Otherwise, we can only include the current element in the subsequence if the remaining subsequence has even weight.
      else:
        table[i][j] = table[i - 1][j - 1]

  # Return the number of k-subsequences with even weight for the entire set.
  return table[m][k]

[m, k] = [int(x) for x in sys.stdin.readline().split()]
count = count_even_weight_subsequences(k, m)

# Print the result.
print(count)