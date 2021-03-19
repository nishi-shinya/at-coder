n = int(input())
W = int(input())

dp = []
# DP初期条件
for w in range(W):
  dp[0][w] = 0

for i in range(n):
  for w in range(W):
    if w >= 
