n = int(input())

arr = []

for _ in range(n):
  arr.append(int(input()))

arr = sorted(arr, reverse=True)

old = 9999999
count = 0

for x in arr:
  if old != x:
    count += 1
    old = x

print(count)
