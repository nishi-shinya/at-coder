import math
import itertools
n,k = map(int, input().split())
arr = []

for x in range(n):
  arr.append(list(map(int, input().split())))

res = list(itertools.permutations(range(1, n)))

count = 0
for perm in res:
  tmp = 0
  old = 0
  for x in perm:
    tmp += arr[old][x]
    old = x
    if tmp > k:
      break
  tmp += arr[old][0]
  if tmp == k:
    count += 1

print(count)
