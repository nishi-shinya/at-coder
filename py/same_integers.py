arr = list(map(int, input().split()))

odd_counter = 0
even_counter = 0
count = 0

for x in arr:
  if x % 2 == 0:
    even_counter += 1
  else:
    odd_counter += 1

if even_counter != 3 and odd_counter != 3:
  if even_counter < odd_counter:
    for i in range(len(arr)):
      if arr[i] % 2 == 1:
        arr[i] += 1
    count += 1
  else:
    for i in range(len(arr)):
      if arr[i] % 2 == 0:
        arr[i] += 1
    count += 1

while (arr[0] != arr[1] or arr[1] != arr[2]):
  min_i = arr.index(min(arr))
  arr[min_i] += 2
  count += 1

print(count)
