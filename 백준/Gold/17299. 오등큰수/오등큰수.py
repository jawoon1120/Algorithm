import sys 
from collections import Counter

n = int(sys.stdin.readline().strip())
input = list(map(int,sys.stdin.readline().strip().split()))
input_counter = Counter(input)
result = [-1]*n
stack = []

for i, e in enumerate(input):
  while stack and stack[-1][0] < input_counter[e]:
    ngf = stack.pop()
    result[ngf[2]] = e
  stack.append((input_counter[e],e,i))

print(*result)
