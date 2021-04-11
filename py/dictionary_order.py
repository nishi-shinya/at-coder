a = input()

length = len(a)

if length > 1:
  print(a[0:length-1])
elif a == 'a':
  print(-1)
else:
  print('a')
