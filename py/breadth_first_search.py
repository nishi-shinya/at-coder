R,C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = []
tmpy, tmpx = sy-1, sx-1
gy, gx = gy-1, gx-1

for i in range(R):
  c.append(list(input()))

que = [[tmpy, tmpx, 0]]

c[tmpy][tmpx] = '0'

res = 0
while(True):
  tmp = que.pop(0)
  tmpy = tmp[0]
  tmpx = tmp[1]
  cnk = tmp[2] + 1

  if tmpy == gy and tmpx == gx:
    res = tmp[2]
    break

  if c[tmpy][tmpx-1] == '.':
    c[tmpy][tmpx-1] = cnk
    que.append([tmpy,tmpx-1,cnk])
  if c[tmpy-1][tmpx] == '.':
    c[tmpy-1][tmpx] = cnk
    que.append([tmpy-1,tmpx,cnk])
  if c[tmpy][tmpx+1] == '.':
    c[tmpy][tmpx+1] = cnk
    que.append([tmpy,tmpx+1,cnk])
  if c[tmpy+1][tmpx] == '.':
    c[tmpy+1][tmpx] = cnk
    que.append([tmpy+1,tmpx,cnk])

print(res)
