c = []
for _ in range(3):
  row = list(map(int, input().split()))
  c.append(row)

a1 = 0
b1 = c[0][0]
b2 = c[0][1]
b3 = c[0][2]
a2 = c[1][0] - b1
a3 = c[2][0] - b1
if c[1][1] - b2 != a2 or c[1][2] -b3 != a2:
  print('No')
  exit()

if c[2][1] - b2 != a3 or c[2][2] - b3 != a3:
  print('No')
  exit()

print('Yes')
