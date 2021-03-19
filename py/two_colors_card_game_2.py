from collections import Counter
n = int(input())
s = []
for x in range(n):
  s.append(input())

s_counter = Counter(s)

m = int(input())
t = []
for x in range(m):
  t.append(input())

t_counter = Counter(t)

s_set = set(s)

res = 0
for x in s_set:
  tmp = s_counter[x]
  if x in t_counter.keys():
    tmp -= t_counter[x]

  res = max(res, tmp)

print(res)
