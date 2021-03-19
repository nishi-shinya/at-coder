n = int(input())

s_arr = []
for x in range(n):
  s_arr.append(input())

m = int(input())

t_arr = []
for x in range(m):
  t_arr.append(input())

tu = set(s_arr)

count = 0
for x in tu:
  tmp = s_arr.count(x)
  tmp_a = t_arr.count(x)
  count = max(count, tmp-tmp_a)

print(count)
