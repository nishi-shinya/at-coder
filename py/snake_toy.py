n,k = map(int, input().split())
l_arr = list(map(int, input().split()))

l_arr = sorted(l_arr, reverse=True)

res = 0

for x in range(k):
  res += l_arr[x]

print(res)
