s = str(input())

for bit in range(2 ** 3):
    tmp = s
    bag = []
    for j in range(3):
        if (bit & (1<<j)):
            bag.append('+')
        else:
          bag.append('-')
    
    tmp_split = list(tmp)

    eval_str = ''
    for i in range(3):
      eval_str += tmp_split[i]
      eval_str += bag[i]

    eval_str += tmp_split[3]

    if eval(eval_str) == 7:
      eval_str += '=7'
      print(eval_str)
      exit()
