def bubble_sort (c,n):
  for i in range(n):
    for j in reversed(range(i,n)):
      if c[j][1] < c[j-1][1]:
        tmp = c[j]
        c[j] = c[j-1]
        c[j-1] = tmp

  return c

def selection_sort (c,n):
  for i in range(n):
    minj = i
    for j in range(i, n):
      if c[j][1] > c[minj][1]:
        minj = j
    tmp = c[minj]
    c[minj] = c[j]
    c[j] = tmp

  return c

def isStable(in_, out):
  for i in range(n):
    for j in range(i,n):
      for a in range()

n = int(input())
a = list(map(str, input().split()))

res = bubble_sort(a,n)
print(res)

res = selection_sort(a,n)
print(res)
