n = int(input())
arr = map(int, input().split())

# [0]: even [1]: odd
res = [0,0]
count = 0

for x in arr:
  if x % 2 == 0:
    res[0] += 1
  else:
    res[1] += 1

if res[1]% 2 == 1:
  print('NO')
else:
  print('YES')
