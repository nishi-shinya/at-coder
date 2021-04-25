abcd = input()

for i in range(2 ** 3):
  tmp = format(i, '03b')
  tmp = tmp.replace('0', '-')
  tmp = tmp.replace('1', '+')
  tmp = list(tmp)

  sum_n = ''
  for p_n, p_o in zip(abcd, tmp + ['']):
    sum_n += p_n + p_o
  if (eval(sum_n)) == 7:
    print(sum_n + '=7')
    break
