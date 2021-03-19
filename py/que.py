n,q = map(int, input().split())
que = []
res = []
i = 0

for x in range(n):
  a,b = map(str, input().split())
  que.append([a, int(b)])

time = 0

while len(que) != 0:
  i %= n
  if que[i][1] < q:
    time += que[i][1]
    que[i][1] -= q
  else:
    time += q
    que[i][1] -= q

  if que[i][1] <= 0:
    print(que[i][0] + ' ' + str(time))
    res.append([que[i][0], time])
    que.pop(i)
    n-=1
    i-=1

  i += 1

# print(res)
