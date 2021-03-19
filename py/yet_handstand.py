import re
n,k = map(int, input().split())
s = input()

m = re.search(r'0+',s)
s[m.start():m.end()] = '0'
print(m.end())
# for x in range(n):
#   if x == '0':
