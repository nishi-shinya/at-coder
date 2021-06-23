s = str(input())
n = len(s) - 1
sum = 0

for bit in range(2 ** n):
    tmp = s
    bag = []
    for j in range(n):
        if (bit & (1<<j)):
            bag.append(j+1)
    
    tmp_split = list(tmp)
    for i in range(len(bag)):
        if i > 0:
            tmp_split.insert(int(bag[i])+i, "+")
        else:
            tmp_split.insert(int(bag[i]), "+")
    sum += eval(''.join(tmp_split))

print(sum)