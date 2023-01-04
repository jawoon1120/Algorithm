import sys
n = int(input())

numbers = [int(sys.stdin.readline().strip()) for _ in range(n)]

stack = []
result = []
number_index = 0

for x in range(1,n+1):
  if x <= numbers[number_index]:  
    stack.append(x)
    result.append("+")
  
  while stack and number_index < len(numbers) and stack[-1] == numbers[number_index]:
    # print(x, result, stack, numbers[number_index])
    stack.pop()
    result.append("-")
    number_index += 1

if stack:
  print("NO")
else:
  [print(r) for r in result]