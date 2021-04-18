n,h = map(int, input().split())
a,b,c,d,e = map(int, input().split())

count = 0
if a > c:
  for i in range(n):
    if h < e:
      h+=d
      count+=c
  count_2 = 0
  for i in range(n):
    if h < e:
      h+=d
      count+=c
else:
  for i in range(n):
    if h < e:
      h+=b
      count+=a
  print(count)
