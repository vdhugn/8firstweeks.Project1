import sys
from collections import defaultdict

[n, m] = [int(x) for x in sys.stdin.readline().split()]
L = []
for i in range(n):
  s = input().strip()
  L.append(s)

hash_table = defaultdict(int)

def hashString(s):
    hashCode=0
    for i in range(len(s)):
        hashCode=hashCode*256+ord(s[i])
        hashCode=hashCode % m
    return hashCode

for s in L:
  hashCode = hashString(s)
  hash_table[hashCode] += 1
  print(hashCode)