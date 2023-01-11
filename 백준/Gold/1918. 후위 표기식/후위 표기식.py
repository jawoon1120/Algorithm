import sys

n = sys.stdin.readline().strip()
result = ''
stack = []
for c in n:
  if c.isalpha():
    result += c
  elif c == "+" or c == "-":
    # 우선순위가 높거나 같으면 pop 이후 push : +,- 는 최하위
    while stack and stack[-1] != "(":
      result += stack.pop()
    stack.append(c)
  elif c == "/" or c == "*":
    while stack and (stack[-1] == "/" or stack[-1] == "*"):
      result += stack.pop()
    stack.append(c)
  elif c == "(":
    stack.append(c)
  elif c == ")":
    while stack and stack[-1] != "(":
      result += stack.pop()
    stack.pop()

print(result+''.join(stack[::-1]))
      