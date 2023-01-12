import sys
input = sys.stdin.readline().strip()
result = [-1]*26

for i, e in enumerate(input): 
  if result[ord(e)-97] == -1:
    result[ord(e)-97]=i
print(*result)