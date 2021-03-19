a,b,c,x,y = map(int, input().split())

c *= 2

res = (a * x) + (b * y)

t = max([x,y])

tmp_res = c * t

if res > tmp_res:
  res = tmp_res

if x < y:
  # aの金額
  tmp_res = (x * c)
  # bの金額
  tmp_res += (y - x) * b
  if res > tmp_res:
    res = tmp_res
elif x > y:
  # aの金額
  tmp_res = (y * c)
  # bの金額
  tmp_res += (x - y) * a
  if res > tmp_res:
    res = tmp_res

print(res)
