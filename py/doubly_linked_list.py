n = int(input())

a = []
for x in range(n):
  command, num = input().split()
  if command == "insert":
    a.insert(0,num)
  elif command == "delete":
    a.remove(num)
  elif command == "deleteFirst":
    a.pop(0)
  elif command == "deleteLast":
    a.pop(-1)

print(' '.join(a))
