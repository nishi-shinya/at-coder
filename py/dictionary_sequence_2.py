n, k = map(int, input().split())
s = list(input())

sorted_s = sorted(s)

print(s)
print(sorted_s)

# tmp_arr = sorted_s[0:k]

# for x in tmp_arr:
#   search_i = s.index(x)
#   s[0], s[search_i] = s[search_i], s[0]
#   s.pop(0)

# print(''.join(tmp_arr) + ''.join(s))
