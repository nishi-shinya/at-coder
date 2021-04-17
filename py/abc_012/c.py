n = int(input())

tmp = 2025 - n

res = []
for x in range(1,10):
  for y in range(1,10):
    if x * y == tmp:
      res.append([str(x) + ' x ' + str(y)])

for x in res:
  print(''.join(x))
