import sys

[n, M] = [int(x) for x in sys.stdin.readline().split()]

def coeficient1(n, M):
  if n == 1:
    return [(M,)]
  collection = []
  for x in range(1, M + 1):
    remaining_collection = coeficient1(n - 1, M - x)
    for e in remaining_collection:
      if e != 0:
        collection.append((x,) + e)
  return collection

def remove_zeroes(collection):
  new_collection = []
  for collection in collection:
    if 0 not in collection:
      new_collection.append(collection)
  return new_collection

s = coeficient1(n, M)
res = remove_zeroes(s)

for element in res:
  print(' '.join(map(str, element)) + ' ')