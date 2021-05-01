n = int(input())
arr = []

a = 0
b = 999999999999999
for _ in range(n):
  tmp = list(map(int, input().split()))
  a = max(a, tmp[1])
  b = min(b, tmp[0])
  arr.append(tmp)

ruiseki = [0] * (a + 2)

for x in arr:
  ruiseki[x[0]] += 1
  ruiseki[x[1]+1] -= 1

tmp = 0
for i in range(len(ruiseki)):
  ruiseki[i] += tmp
  tmp = ruiseki[i]

print(max(ruiseki))
# res = 0
# count = 0
# for i in range(min_t, max_t+1):
#   tmp = 0
#   for x in arr:
#     if i in x:
#       tmp += 1
#   if count <= tmp:
#     count = tmp
#     res = i

# print(res+1)
