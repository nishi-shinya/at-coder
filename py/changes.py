n = int(input())
a = ["1","2","3","4","5","6"]

if n > 30:
  n %= 30

i = 0
for i in range(n):
  tmp = (i % 5) + 1
  a[tmp-1], a[tmp] = a[tmp], a[tmp-1]

print("".join(a))
