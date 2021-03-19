n = int(input())
res = set()

for x in range(1, int(pow(n, 0.5) + 1)):
  if n % x == 0:
    res.add(x)
    res.add(n // x)

res = sorted(res)

for x in res:
  print(x)

