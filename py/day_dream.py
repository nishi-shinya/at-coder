s = input()
str = "dream dreamer erase eraser"
str = str.split()

str = sorted(str, reverse=True)

for x in str:
  s = s.replace(x, '')

if s == '':
  print("YES")
else:
  print("NO")
