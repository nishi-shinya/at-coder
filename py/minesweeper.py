h,w = map(int, input().split())
arr = []
tmp_arr = []
x_arr = [1,0,-1]
y_arr = [1,0,-1]

for i in range(h):
  tmp = list(input())
  arr.append(tmp)
  # tmp_arr.append([j for j, x in enumerate(tmp) if x == '#'])

for x in x_arr:
  for y in y_arr:
    
# for x in range(len(tmp_arr)):
#   for y in range(len(tmp_arr[x])):
#     if tmp_arr[x][y] < 0:
    
#     if tmp_arr[x][y] == w:


print(arr)
