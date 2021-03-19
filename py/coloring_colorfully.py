s = input()

start = s[0]

count = 0
if start == '0':
  for i in range(len(s)):
    if i % 2 == 1 and s[i] == '0':
      count += 1
    elif i % 2 == 0 and s[i] == '1':
      count += 1
elif start == '1':
  for i in range(len(s)):
    if i % 2 == 1 and s[i] == '1':
      count += 1
    elif i % 2 == 0 and s[i] == '0':
      count += 1

print(count)


