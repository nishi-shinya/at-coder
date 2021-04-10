n = int(input())
takoyaki = []

for i in range(n):
  takoyaki.append(int(input()))

takoyaki = sorted(takoyaki)
print(takoyaki[0])
