n = int(input())
a = list(map(int, input().split()))

max_tmp = max(a)
res = 0

for x in range(2, max_tmp+1):
  tmp = 0
  tmp_res = 0
  for y in a:
    tmp_res = y
    if y % x == 0:
      tmp += 1
  res = max(tmp,res)

print(res)
