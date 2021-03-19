n = int(input())
a = list(map(int, input().split()))

count = 0
flg = False
for x in range(1, n):
  if a[x-1] > a[x] and flg:
    count += 1
    flg = False
  if a[x-1] < a[x] and not flg:
    flg = True

print(count)
