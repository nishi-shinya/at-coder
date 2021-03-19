n,x = map(int, input().split())
a = list(map(str, input().split()))

res = []
for i in range(n):
  if a[i] != str(x):
    res.append(a[i])

print(' '.join(res))
