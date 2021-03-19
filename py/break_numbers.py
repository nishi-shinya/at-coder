n = int(input())

def loop(x):
  global n
  tmp = x * 2
  if n > tmp:
    tmp = loop(tmp)
  else:
    tmp = loop(tmp / 2)

  return tmp


res = loop(1)
print(res)

# flg = True
# x = 1
# while flg:
#   tmp = x * 2
#   if n < tmp:
#     flg = False
#     break

#   x = tmp

# print(x)
