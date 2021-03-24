x1,y1,x2,y2 = map(int, input().split())

tmp1 = x2 - x1
tmp2 = y1 + y2

tmp3 = tmp1 / tmp2

print(round(tmp3 * y1 + x1, 10))
