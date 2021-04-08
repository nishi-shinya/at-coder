Xa,Ya,Xb,Yb,Xc,Yc = map(int, input().split())

tmp = ((Xb - Xa) * (Yc - Ya)) - ((Yb - Ya) * (Xc - Xa))

print(abs(tmp)/2)
