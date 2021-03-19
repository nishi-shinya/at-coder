n = int(input())
a_arr = list(map(int, input().split()))
d = 0
ans = 1
for i in range(n-1):
  b = a_arr[i+1] - a_arr[i]
  if d * b < 0:
    ans += 1
    d = 0
  elif d == 0:
    d = b

print(ans)

