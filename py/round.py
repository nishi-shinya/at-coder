c = []

for i in range(4):
  c.append(input().split())

for i in range(len(c)):
  c[i][0], c[i][-1] = c[i][-1], c[i][0]
  c[i][1], c[i][-2] = c[i][-2], c[i][1]

c[0],c[3] = c[3], c[0]
c[1],c[2] = c[2], c[1]

for x in c:
  print(' '.join(x))
