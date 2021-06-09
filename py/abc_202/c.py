n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

cnt = 0

for a_tmp in a:
  tmp = [i+1 for i, x in enumerate(b) if x == a_tmp]
  for y in tmp:
    cnt += len([i for i, x in enumerate(c) if x == y])
    
print(cnt)
    