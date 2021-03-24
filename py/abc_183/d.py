n,w = map(int, input().split())
arr = [0 for _ in range(0,(2*(10**5)+1))]

for x in range(n):
  tmp = list(map(int, input().split()))
  arr[tmp[0]] += tmp[2]
  arr[tmp[1]] -= tmp[2]

for i in range(len(arr)-1):
  arr[i+1] += arr[i]
  if arr[i] > w:
    print('No')
    exit()

print('Yes')
