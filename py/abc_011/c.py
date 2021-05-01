n = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())
arr = sorted([NG1,NG2,NG3], reverse=True)
i = 0
count = 0
tmp = n
flg = False
if not n in arr:
  for _ in range(100):
    if tmp-3 in arr:
      if tmp-2 in arr:
        if tmp-1 in arr:
          flg = False
          break
        else:
          tmp -= 1
      else:
        tmp -= 2
    else:
      tmp -= 3
    count+=1
    if tmp <= 0:
      flg = True
      break

if flg:
  print('YES')
else:
  print('NO')
