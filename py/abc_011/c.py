n = int(input())
NG1 = int(input())
NG2 = int(input())
NG3 = int(input())
arr = sorted([NG1,NG2,NG3], reverse=True)
i = 0
count = 0
tmp = n
flg = True
for x in range(100):
  if (n - 3) == arr[i] or (n - 2) == arr[i] or (n - 1) == arr[i]:
    if (n-3) == arr[i]:
      if (n-2) == arr[i+1]:
        
  tmp-=3
  count+=1
  if tmp <= 0:
    break

if flg:
  print('YES')
else:
  print('NO')
