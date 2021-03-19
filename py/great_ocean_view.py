n = int(input())
h = list(map(int, input().split()))

m = 0
count = 0
for x in h:
  if m <= x:
    count += 1
    m = x

print(count)
