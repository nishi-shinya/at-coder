n = input()
a_arr = list(map(int, input().split()))

flg = True

count = 0

while flg:
  for index in range(len(a_arr)):
    if a_arr[index] % 2 == 0:
      a_arr[index] = a_arr[index] / 2
      a_arr[index] = int(a_arr[index])
    else:
      flg = False
      break

  if flg:
    count += 1

print(count)
