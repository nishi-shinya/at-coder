n = int(input())
a = list(map(int, input().split()))

q = int(input())
m = list(map(int, input().split()))

def solve (i, m):
  global n
  print(m)
  if (m == 0):
    return 1
  if (i <= n):
    return 0
  res = solve (i + 1 ,m) or solve(i + 1, m - a[i])
  return res

for x in m:
  if solve(0, x):
    print('Yes')
  else:
    print('No')

