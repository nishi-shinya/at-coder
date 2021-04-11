n, m = map(int, input().split())

a,b,c = 0,0,0

if m % 2 == 1:
  b = 1
  a = n - 1
  while (True):
    if a <= -1:
      print(-1,-1,-1)
      break
    if (2*a)+(3*b)+(4*c) == m:
      print(a,b,c)
      break
    c += 1
    a -= 1
else:
  b = 0
  a = n
  while (True):
    if a <= -1:
      print(-1,-1,-1)
      break
    if (2*a)+(3*b)+(4*c) == m:
      print(a,b,c)
      break
    c += 1
    a -= 1
