from collections import deque
import sys


n = int(input())
commands = [sys.stdin.readline().strip().split() for _ in range(n)]

def pop(deque):
  return -1 if not deque else deque.pop()
# def size():

def empty(deque):
  return 1 if not deque else 0
def front(deque):
  return deque[-1] if deque else -1
def back(deque):
  return deque[0] if deque else -1


deque = deque()
result = []
for command in commands:
  if command[0] == "push":
    deque.appendleft(command[1])
  if command[0] == "pop":
    result.append(pop(deque))
  if command[0] == "size":
    result.append(len(deque))
  if command[0] == "empty":
    result.append(empty(deque))    
  if command[0] == "front":
    result.append(front(deque))
  if command[0] == "back":
    result.append(back(deque))
  
[print (r) for r in result]