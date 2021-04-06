n = int(input())
s = input()

tmp = s.count("E")
res = 10**9
for i in range(n):
  if s[i] == 'E':
    tmp -= 1
  res = min(res, tmp)
  if s[i] == 'W':
    tmp += 1

print(res)
