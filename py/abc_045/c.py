s = list(input())
n = len(s)

sum_n = 0
for i in range(2 ** (n-1)):
  tmp = [''] * (n - 1)
  for j in range(n-1):
    if ((i >> j) & 1):
      tmp[j] = '+'
  formula = ''
  for a,b in zip(s, tmp + ['']):
    formula += a + b
  sum_n += eval(formula)

print(sum_n)
