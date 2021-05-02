from collections import Counter
n,m = map(int, input().split())
ab = {}

ruiseki = [0] * n

for i in range(m):
  a,b = map(int, input().split())
  if not ab.get(a):
    ab[a] = [b]
  else:
    ab[a].append(b)

print(ab)

