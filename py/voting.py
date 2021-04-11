n = int(input())
s = []

for i in range(n):
  s.append(input())

set_s = set(s)

max_res = 0
max_str = ''
for x in set_s:
  tmp = s.count(x)
  if max_res < tmp:
    max_res = tmp
    max_str = x

print(max_str)
