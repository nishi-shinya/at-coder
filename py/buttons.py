a,b = map(int,input().split())

res = 0
for x in range(2):
  if a > b:
    res += a
    a -= 1
  else:
    res += b
    b -= 1

print(res)
