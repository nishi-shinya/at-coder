s = input()

tmp = ''
for i in range(len(s)):
  if i == 0:
    tmp += s[i].upper()
  else:
    tmp += s[i].lower()

print(tmp)
