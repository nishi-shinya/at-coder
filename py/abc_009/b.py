n = int(input())

a = [int(input()) for _ in range(n)]

set_a = []
for x in a:
  if not x in set_a:
    set_a.append(x)

set_a = sorted(set_a)
print(set_a[-2])
