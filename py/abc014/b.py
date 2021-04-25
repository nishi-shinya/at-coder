n,x = map(int, input().split())
a = list(map(int, input().split()))
a.reverse()
bit_x = format(x,'b')
bit_x = bit_x.rjust(n,'0')

res = 0
i = -1
while(True):
  if bit_x[i] == '1':
    res += a[i]
  if abs(i) == n:
    break
  i-=1

print(res)
