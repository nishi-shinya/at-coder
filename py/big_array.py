n,k = map(int, input().split())

res = []
for x in range(n):
  a,b = map(int, input().split())
  res.append([a,b])

res.sort()
tmp_a = k

for x in res:
  tmp_a -= x[1]
  if tmp_a <= 0:
    print(x[0])
    break
