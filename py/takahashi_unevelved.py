x,y,a,b = map(int, input().split())

exp = 0

while y >= x:
  if x > y / a:
    break
  if a*x >= y:
    break
  if a*x >= x+a:
    break
  if x < b / a - 1:
    x *= a
    exp += 1
  else:
    x += b
    exp += 1

print(exp)
