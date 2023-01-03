import sys
n = int(input())

# valid_vps (ps:str) -> str
def valid_vps(ps):
  stack = []
  for parenthesis in ps:
    if not stack:
      stack.append(parenthesis)
    elif stack[-1] == '(' and parenthesis == '(':
      stack.append(parenthesis)
    elif stack[-1] == '(' and parenthesis == ')':
      stack.pop()

  return 'NO' if stack else 'YES' 
  
pss = [sys.stdin.readline().strip() for _ in range(n)]
[print(valid_vps(ps)) for ps in pss]