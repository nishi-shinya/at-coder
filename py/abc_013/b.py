a = int(input())
b = int(input())
arr = [0,1,2,3,4,5,6,7,8,9]
ind = arr.index(a)
tmp = ind
count_1 = 0
while(arr[tmp] != b):
  tmp+=1
  if tmp > 9:
    tmp = 0
  count_1+=1
tmp = ind
count_2 = 0
while(arr[tmp] != b):
  tmp-=1
  count_2+=1

print(min(count_1,count_2))
