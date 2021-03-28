from collections import Counter
n = int(input())
arr = []
count = 0
for _ in range(n):
  arr.append(int(input()))

counter = Counter(arr)

for x in counter.values():
  if x % 2 == 1:
    count += 1

print(count)
