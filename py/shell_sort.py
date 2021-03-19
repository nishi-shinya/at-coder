def insertion_sort(a,n,g):
  for i in range(g,n):
    v = a[i]
    j = i - g
    while j >= 0 and a[j] > v:
      a[j+g] = a[j]
      j = j - g
      cnt += 1
    a[j+g] = v

def shell_sort(a,n):
  cnt = 0
  m = 
