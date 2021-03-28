from collections import Counter
n = int(input())
a = list(map(int, input().split()))

counter = Counter(a)

res = 0
for x in counter.keys():
  tmp = 0
  if x - 1 in counter:
    tmp += counter[x-1]
  if x in counter:
    tmp += counter[x]
  if x + 1 in counter:
    tmp += counter[x+1]

  res = max(res, tmp)

print(res)
