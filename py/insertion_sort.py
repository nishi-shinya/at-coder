n = int(input())

arr = list(map(int, input().split()))

def insertion_sort(a,n):
  for i in range(n):
    tmp = a[i]
    prev = i - 1
    while prev >= 0 and a[prev] > tmp:
      # 右にずらす
      a[prev+1] = a[prev]
      prev -= 1
    a[prev+1] = tmp
    print(a)

insertion_sort(arr, n)
