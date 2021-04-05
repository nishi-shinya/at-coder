a,b,c = map(int, input().split())

count = 1
flg = True
while (flg):
  tmp = a * count
  if tmp % b == c:
    flg = False
  if count == 100:
    break
  count += 1

if not flg:
  print('YES')
else:
  print('NO')
