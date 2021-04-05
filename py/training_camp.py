n = int(input())

res = 1
for x in range(1, n+1):
  res = (res * x) % 1000000007

print(res)
