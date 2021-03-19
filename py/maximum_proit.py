n = int(input())

arr = []
for x in range(n):
  arr.append(int(input()))

res = -20000000
minv = arr[0]
for x in range(1,len(arr)):
  res = max(res, arr[x] - minv)
  minv = min(minv, arr[x])

print(res)
