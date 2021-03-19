def reverse_poland(string):
  string = string.split(' ')
  stack = []
  for i in range(len(string)):
    if string[i] == '+' or string[i] == '-' or string[i] == '*' or string[i] == '/':
      if string[i] == '+':
        tmp = stack.pop(-1)
        tmp_2 = stack.pop(-1)
        stack.append(tmp_2 + tmp)
      if string[i] == '-':
        tmp = stack.pop(-1)
        tmp_2 = stack.pop(-1)
        stack.append(tmp_2 - tmp)
      if string[i] == '*':
        tmp = stack.pop(-1)
        tmp_2 = stack.pop(-1)
        stack.append(tmp_2 * tmp)
      if string[i] == '/':
        tmp = stack.pop(-1)
        tmp_2 = stack.pop(-1)
        stack.append(tmp_2 / tmp)
    else:
      stack.append(int(string[i]))

  return stack[0]

stri = reverse_poland('1 2 + 3 4 - *')
print(stri)
