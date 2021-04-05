n = int(input())
a = []
for x in range(n):
  a.append(int(input()))

i = 1
count = 0
flg = True
while(flg):
  if i == 2:
    flg = False
    break

  i = a[i-1]
  if count == len(a):
    break
  count += 1

if not flg:
  print(count)
else:
  print(-1)
