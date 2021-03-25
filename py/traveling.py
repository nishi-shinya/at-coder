n = int(input())
arr = []

for x in range(n):
  arr.append(list(map(int, input().split())))

old_time = 0
old_total = 0
for a in arr:
  time = a[0]
  x = a[1]
  y = a[2]
  total = x + y
  # 移動距離
  distance = abs(x) + abs(y)
  if time < distance:
    print('No')
    exit()
  if old_total - total > time - old_time:
    print('No')
    exit()
  if total % 2 == 0 and time % 2 == 1:
    print('No')
    exit()
  elif total % 2 == 1 and time % 2 == 0:
    print('No')
    exit()

  old_time = time
  old_total = total

print('Yes')
