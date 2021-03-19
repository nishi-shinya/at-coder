n = int(input())
res = 100000
t = int(n**0.5)
for a in range(1, t + 1):
  if n % a == 0:
    b = n // a
    if b >= a:
      tmp = len(str(int(b)))
      if res > tmp:
        res = tmp
    elif b < a:
      tmp = len(str(int(a)))
      if res > tmp:
        res = tmp

print(res)
