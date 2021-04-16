n = int(input())
a = list(map(int, input().split()))

count = 0
for x in a:
  if x % 6 == 0:
    count += 3
    continue
  if x % 5 == 0:
    count += 2
    continue
  if x % 2 == 0:
    count += 1

print(count)
