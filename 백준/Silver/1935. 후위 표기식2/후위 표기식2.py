import sys

n = int(sys.stdin.readline().strip())
fx = sys.stdin.readline().strip()
num_map = {chr(i+65):int(sys.stdin.readline().strip()) for i in range(n)} 
stack = []

for e in fx:
  if e.isalpha():
    stack.append(num_map[e])
  elif e == "+":
    stack.append(stack.pop()+stack.pop())
  elif e == "-":
    stack.append(-stack.pop()+stack.pop())
  elif e == "/":
    first = stack.pop()
    stack.append(stack.pop()/first)
  elif e == "*":
    stack.append(stack.pop()*stack.pop())

print(f"{stack[0]:.2f}")
