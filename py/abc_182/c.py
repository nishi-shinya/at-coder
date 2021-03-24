n = list(input())
arr = [{0:0},{1:0},{2:0}]

# 組み合わせの数
for x in n:
  tmp = int(x) % 3
  arr[tmp].add(arr[tmp] + 1)

# if sum(arr) % 3 == 0:
#   print(0)
#   exit()
# elif sum(arr) % 3 == 1:
#   print(1)
#   exit()
# else:
#   if 2 in arr:
#     print(1)
#     exit()
#   else:
#     if arr.count(1) <= 2 and len(arr) != 2:
#       print(2)
#       exit()
#     else:
#       print(-1)
#       exit()
