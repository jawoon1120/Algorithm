input = input()

stack=[]
stick_count = 0
for i, e in enumerate(input):
  if e == '(':
    stack.append(e)
  elif e == ')':
    if input[i-1] == '(':
      stack.pop()
      stick_count += len(stack) 
    elif stack[-1] == '(':
      stick_count +=1
      stack.pop()

print(stick_count)