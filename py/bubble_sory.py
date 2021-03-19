def bubble_sort(a,n):
  flg = 1
  count = 0
  while flg:
    flg = 0
    for j in reversed(range(1, n)):
      if a[j] < a[j-1]:
        tmp = a[j-1]
        a[j-1] = a[j]
        a[j] = tmp
        flg = 1
        count += 1
  
  a = map(str, a)
  print(' '.join(a))
  print(count)

n = int(input())
a = list(map(int, input().split()))

bubble_sort(a,n)



