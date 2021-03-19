def selection_sort(a,n):
  count = 0
  for i in range(0, n):
    minj = i
    for j in range(i, n):
      if a[j] < a[minj]:
        minj = j
    if a[i] != a[minj]:
      count += 1
    tmp = a[i]
    a[i] = a[minj]
    a[minj] = tmp

  return [a, count]
n = int(input())
a = list(map(int, input().split()))

res = selection_sort(a,n)
st = list(map(str, res[0]))
print(' '.join(st))
print(res[1])
