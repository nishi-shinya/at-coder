s = input()

i = [chr(ord('a') + i) for i in range(26)]

res = ''
for x in i:
  if not x in s:
    res = x
    break

if res == '':
  res = 'None'
print(res)
