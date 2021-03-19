w,h,n = map(int, input().split())

xmin=0
xmax=w
ymin=0
ymax=h

arr = []
for x in range(n):
  arr.append(list(map(int, input().split())))


for x in arr:
  if x[2] == 1:
    xmin=max(xmin,x[0])
  elif x[2] == 2:
    xmax=min(xmax,x[0])
  elif x[2] == 3:
    ymin=max(ymin,x[1])
  elif x[2] == 4:
    ymax=min(ymax,x[1])

print((max(xmax-xmin,0)*max(ymax-ymin,0)))
