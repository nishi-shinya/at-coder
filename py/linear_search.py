n = int(input())
S = list(map(int, input().split()))

q = int(input())
T = list(map(int, input().split()))

res = 0
for x in S:
  res += T.count(x)

print(res)
