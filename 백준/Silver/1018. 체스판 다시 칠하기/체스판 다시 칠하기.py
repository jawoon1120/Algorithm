import sys
from itertools import product

def check_line(line_i,i,e,first_color, second_color):
  modi_count=0
  if line_i % 2 == 0:
    if i % 2 == 0 and e != first_color:
      modi_count += 1
    elif i % 2 != 0 and e != second_color:
      modi_count += 1
  elif line_i % 2 != 0:
    if i % 2 == 0 and e != second_color:
      modi_count += 1
    elif i % 2 != 0 and e != first_color:
      modi_count += 1
  return modi_count
    
m, n = map(int,sys.stdin.readline().split())
# 시작점 조합
start_point= list(product(range(m+1-8),range(n+1-8)))
board = [ sys.stdin.readline().strip() for _ in range(m)]
result = []

for start_m, start_n in start_point:
  black_start = 0
  white_start = 0
  for line_i,line in enumerate(board[start_m:start_m+8]):
    for i, e in enumerate(line[start_n:start_n+8]):
      black_start += check_line(line_i,i,e,"B","W")
      white_start += check_line(line_i,i,e,"W","B")
  result.append(black_start)
  result.append(white_start)
print(min(result))