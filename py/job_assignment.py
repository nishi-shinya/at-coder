n = int(input())

a_arr = []
b_arr = []
for x in range(n):
  a,b = map(int, input().split())
  a_arr.append(a)
  b_arr.append(b)

ans = 10**6
for i in range(n):
  for j in range(n):
    if i == j:
      ans = min(ans, a_arr[i] + b_arr[j])
    else:
      ans = min(ans, max(a_arr[i], b_arr[j]))

print(ans)
