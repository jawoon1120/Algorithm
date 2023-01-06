import re
import sys

lines = []
while True:
    line = sys.stdin.readline().replace('\n','')
    lines.append(line)
    if line == '.':
        break
    
def valid_balance(line):
  stack =[]
  for char in line:
    if not stack:
      stack.append(char)
    elif char==')' and stack[-1]=='(':
      stack.pop()
    elif char==']' and stack[-1]=='[':
      stack.pop()
    else:
      stack.append(char)
  return 'yes' if not stack else 'no'

modi_lines = [re.sub('[a-zA-Z. ]',"",line) for line in lines]
modi_lines.pop()
results = [ valid_balance(ml) for ml in modi_lines]
[ print(r) for r in results]