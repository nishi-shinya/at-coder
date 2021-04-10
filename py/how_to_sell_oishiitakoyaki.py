t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

flg = False
cnt = 0
if m <= n:
  for i in range(n):
    tmp1 = a[i]
    tmp2 = a[i] + t
    for j in range(m):
      if tmp1 <= b[j] and b[j] <= tmp2:
        cnt += 1
        b[j] = 0
        break
      elif b[j] < tmp1:
        continue

    if m <= cnt:
      break

  if m == cnt:
    flg = True

if flg:
  print('yes')
else:
  print('no')

