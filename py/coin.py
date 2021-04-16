n = int(input())
c = []

for i in range(n):
  c.append(int(input()))

for j in range(n):
  for k in range(j,n):
    if j == k:
      continue
    if arr[k] % arr[j] == 0:
      coin[k] = int(not coin[k])

print('{:.10f}'.format(res))
