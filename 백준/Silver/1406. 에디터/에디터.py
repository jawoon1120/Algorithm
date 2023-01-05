import sys
cursor_left_side = list(input())
cursor_right_side = []

m = int(input())
commands = [sys.stdin.readline().strip().split() for _ in range(m)] 

def move_left(cursor_left_side, cursor_right_side):
  if cursor_left_side:
    cursor_right_side.append(cursor_left_side.pop())
def move_right(cursor_left_side, cursor_right_side):
  if cursor_right_side:  
    cursor_left_side.append(cursor_right_side.pop())
def del_left(cursor_left_side):
  if cursor_left_side:
    cursor_left_side.pop()
def add_left(cursor_left_side, value):
  cursor_left_side.append(value)


for command in commands:
  if command[0] == "L":
    move_left(cursor_left_side, cursor_right_side)
  if command[0] == "D":
    move_right(cursor_left_side, cursor_right_side)
  if command[0] == "B":
    del_left(cursor_left_side)
  if command[0] == "P":
    add_left(cursor_left_side, command[1])


print(''.join(cursor_left_side)+''.join(cursor_right_side[::-1]))