x,a,b = map(int, input().split())

a_diff = abs(x - a)
b_diff = abs(x - b)

if a_diff > b_diff:
  print('B')
  exit()

print('A')
