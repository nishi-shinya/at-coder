n = int(input())
a = ["1","2","3","4","5","6"]

t = len(str(n))
if t >= 3:
  o = "1" + ("0" * (t-3))
  n %= int(o)
  n %= 30

i = 0
while(True):
  tmp = (i % 5) + 1
  a[tmp-1], a[tmp] = a[tmp], a[tmp-1]
  i += 1
  if n == i:
    break

print("".join(a))
