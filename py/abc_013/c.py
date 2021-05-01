n,h = map(int, input().split())
a,b,c,d,e = map(int, input().split())

tmp = h
amount = 0
for i in range(n):
  if tmp <= e:
    tmp += d
    amount += c
amount_2 = 0
for i in range(n):

print(amount)
