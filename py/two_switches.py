a,b,c,d = map(int, input().split())

if a < c:
  if b < c:
    print(0)
  elif d < b:
    print(d-c)
  else:
    print(b-c)
else:
  if d < a:
    print(0)
  elif b < d:
    print(b-a)
  else:
    print(d-a)
