n = int(input())
h = n // 3600
m = (n-(3600*h)) // 60
s = n % 60

print(
  '{:02}'.format(h) + ':' +
  '{:02}'.format(m) + ':' +
  '{:02}'.format(s)
)
