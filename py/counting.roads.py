n,m = map(int, input().split())

res = []
for x in range(m):
  a, b = map(int, input().split())
  res.append(a)
  res.append(b)

for x in range(1, n + 1):
  print(res.count(x))
