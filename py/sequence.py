n = int(input())
a = list(map(int, input().split()))

ans = [0,0]

for i in range(2):
  total = 0
  for j in range(n):
    total += a[j]
    if (i + j) % 2 == 0:
      if total <= 0:
        ans[i] += abs(total-1)
        total = 1




print(count)
