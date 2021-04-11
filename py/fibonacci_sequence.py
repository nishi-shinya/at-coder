n = int(input())
a = 0
b = 0
c = 1
for i in range(n-1):
  tmp = a + b + c%10007
  a,b,c = b%10007,c%10007,tmp

print(a%10007)
