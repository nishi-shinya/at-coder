n = int(input())

res = 0
for i in range(n):
  a,b = map(int,input().split())
  # 数列の数
  n = b - a + 1
  if n % 2 == 1:
    res += ((b + a) * (n // 2)) + ((b + a) // 2)
  else:
    res += (b + a) * (n // 2)

print(res)
