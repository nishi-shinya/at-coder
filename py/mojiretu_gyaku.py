def reverse_str (str, str_1=''):
  if len(str) == len(str_1):
    return str_1
  str_1 += str[(len(str)-1) - len(str_1)]
  return reverse_str(str, str_1)


tmp = reverse_str('recursion')
print(tmp)
tmp = reverse_str('i am a software engineer')
print(tmp)
