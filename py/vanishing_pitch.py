v,t,s,d = map(int, input().split())

tmp = d / v

if t <= tmp and tmp <= s:
  print('No')
else:
  print('Yes')
