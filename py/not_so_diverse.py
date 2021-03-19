from collections import Counter
n,k = map(int, input().split())
a = list(map(int, input().split()))

ball = Counter(a)
counter = sorted(ball.items(), key=lambda x: x[1])
tmp = len(counter)
count = 0
if k < tmp:
  for key, y in counter:
    count += y
    tmp -= 1
    if k == tmp:
      break

print(count)
