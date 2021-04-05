n = int(input())
a = []

a.append(list(map(int, input().split())))
a.append(list(map(int, input().split())))

mx = 0
for i in range(n):
  tmp = 0
  x = 0
  y = 0
  tmp += a[x][y]
  for j in range(n):
    if i == j:
      x += 1
    else:
      y += 1
    tmp += a[x][y]

  mx = max(tmp, mx)

print(mx)
