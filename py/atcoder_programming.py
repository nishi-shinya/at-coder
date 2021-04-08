n,k = map(int, input().split())
r = list(map(int, input().split()))

r = sorted(r)

tmp = n-k
c = 0
for i in range(tmp, n):
  c = (c + r[i]) / 2
print('{:.7f}'.format(c))
