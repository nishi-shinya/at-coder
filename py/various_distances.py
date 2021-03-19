n = int(input())
x = list(map(int, input().split()))

absX = list(map(abs, x))
absX2 = list(k*k for k in x)

print(sum(absX))
print((sum(absX2))**0.5)
print(max(absX))
