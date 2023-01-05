from collections import deque
import sys
n = int(input())

commands = [sys.stdin.readline().strip().split() for _ in range(n)]

def pop_front(deque):
  return -1 if not deque else deque.popleft()
def pop_back(deque):
  return -1 if not deque else deque.pop()
def empty(deque):
  return 1 if not deque else 0
def front(deque):
  return -1 if not deque else deque[0]
def back(deque):
  return -1 if not deque else deque[-1]

deque = deque()
result = []

for command in commands:
  if command[0] == "push_front":
    deque.appendleft(command[1])
  elif command[0] == "push_back":
    deque.append(command[1])
  elif command[0] == "pop_front":
    result.append(pop_front(deque))
  elif command[0] == "pop_back":
    result.append(pop_back(deque))
  elif command[0] == "size":
    result.append(len(deque))
  elif command[0] == "empty":
    result.append(empty(deque))
  elif command[0] == "front":
    result.append(front(deque))
  elif command[0] == "back":
    result.append(back(deque))

[print(r) for r in result]