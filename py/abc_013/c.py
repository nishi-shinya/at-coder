n,h = map(int, input().split())
a,b,c,d,e = map(int, input().split())

x = n
y = 0
for i in range(n):
  if h + (b*x) + (d*y) - (n - x - y) * e > 0:
    
