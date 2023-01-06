import sys
from collections import deque

test_case_count = int(sys.stdin.readline().strip())

result = []
for _ in range(test_case_count):
  n, target = map(int,sys.stdin.readline().strip().split())
  priorities = deque( [(int(q),i) for i,q in enumerate(sys.stdin.readline().strip().split())])
  # print(priorities)
  print_count = 0
  while True:
    best = max(priorities)[0]
    print_turn = priorities.popleft()
    
    # print(print_turn,best,target,print_count)
      
    if print_turn[0] == best:
      print_count += 1
      if print_turn[1] == target:
        result.append(print_count)
        break
    else:
      priorities.append(print_turn)
    
[print(r) for r in result]