a,b = map(int,input().split())

tmp = (a * 2) + 100

res = tmp - b

if res <= 0:
  print(0)
else:
  print(res)
