import sys

n = int(input().strip())
command = [sys.stdin.readline().strip() for x in range(n)]

stack = []
def exe_command(t_stack,command):
  if command[0] == 'push':
    t_stack.append(command[1])
    return;
  elif command[0] == 'pop':
    return -1 if not t_stack else t_stack.pop()
  elif command[0] == 'size':
    return len(t_stack)
  elif command[0] == 'empty':
    return 1 if not t_stack else 0
  elif command[0] == 'top':
    return -1 if not t_stack else t_stack[-1]
    
result = [exe_command(stack,c.split()) for c in command]

[print(r) for r in result if r != None]