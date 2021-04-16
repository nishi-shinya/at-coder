Txa, Tya, Txb, Tyb, T, V = map(int, input().split())
n = int(input())
arr = []
for x in range(n):
  arr.append(list(map(int, input().split())))

X = Txa
Y = Tya

distance = 0
flg = False
for x in arr:
  tmp1 = ((x[0]-X)**2)
  tmp2 = ((x[1]-Y)**2)
  distance += (tmp1+tmp2)**0.5
  tmp1 = ((Txb-x[0])**2)
  tmp2 = ((Tyb-x[1])**2)
  distance += (tmp1+tmp2)**0.5
  if (T*V) >= distance:
    flg = True
  distance = 0

if flg:
  print('YES')
else:
  print('NO')
