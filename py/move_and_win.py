n,a,b = map(int, input().split())

arr = [a,b]
alice = True
while (True):
  if arr[0] == arr[1] - 1:
    break
  for i in range(len(arr)):
    if i == 0:
      arr[i] += 1
      alice = False
    else:
      arr[i] -= 1
      alice = True
    if arr[0] == arr[1] - 1:
      break

if alice:
  print('Borys')
else:
  print('Alice')
