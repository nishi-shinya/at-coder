s = input()
t = input()

arr = ['a','t','c','o','d','e','r']

chk = True
for i in range(len(s)):
  tmp1 = s[i]
  tmp2 = t[i]
  if tmp1 == '@' and tmp2 == '@':
    continue
  elif tmp1 == '@':
    if not tmp2 in arr:
      chk = False
      break
  elif tmp2 == '@':
    if not tmp1 in arr:
      chk = False
      break
  elif tmp1 != tmp2:
    chk = False
    break

if chk:
  print('You can win')
else:
  print('You will lose')
