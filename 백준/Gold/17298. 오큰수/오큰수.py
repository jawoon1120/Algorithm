import sys

n = int(sys.stdin.readline().strip())
array = list(map(int,sys.stdin.readline().strip().split()))
stack = []
result = [-1]*n

for i,e in enumerate(array):
  while stack and e > stack[-1][1]:
    # print(stack,result)
    prev_i, _ = stack.pop()
    result[prev_i] = e
  stack.append((i,e))

print(*result)