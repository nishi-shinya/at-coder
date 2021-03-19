n = int(input())
a = list(map(int, input().split()))

res = 0
res_2 = 0
for i in range(n):
  res += a[i] ** 2
  res_2 += a[i]

print(n * res - res_2 ** 2)
