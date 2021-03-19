str = input()

divide = ['dream', 'dreamer', 'erase', 'eraser']

dp = []

dp[0] = 1

for i in len(str):
  if not dp[i] : continue
  for s in divide:
    if str[i:len(str)] == s:
      dp[i + len(str)] = 1

print(dp[len(str)])


