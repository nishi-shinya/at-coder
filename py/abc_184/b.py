n,x = map(int, input().split())
s = input()

for i in range(len(s)):
  if s[i] == 'o':
    x += 1
  elif s[i] == 'x' and x > 0:
    x -= 1

print(x)
