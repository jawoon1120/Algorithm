import sys
from itertools import product

def check_line(line_i, i, e, first_color):
  modi_count = 0
  # 0,2,4,6 번째 M
  if line_i % 2 == 0:
    # 0,2,4,6 번째 N 인데 시작 색과 다른 경우 수정 필요
    if i % 2 == 0 and e != first_color:
      modi_count += 1
    # 1,3,5,7 번째 N 인데 시작 색과 같은 경우 수정 필요
    elif i % 2 != 0 and e == first_color:
      modi_count += 1
  # 1,3,5,7 번째 N
  elif line_i % 2 != 0:
    # 0,2,4,6 번째 N 인데 시작 색과 같은 경우 수정 필요
    if i % 2 == 0 and e == first_color:
      modi_count += 1
    # 1,3,5,7 번째 N 인데 시작 색과 다른 경우 수정 필요
    elif i % 2 != 0 and e != first_color:
      modi_count += 1
  return modi_count
    
m, n = map(int,sys.stdin.readline().split())
# 시작점 조합
start_point= list(product(range(m + 1 - 8),range(n + 1 - 8)))
board = [ sys.stdin.readline().strip() for _ in range(m)]
result = []

for start_m, start_n in start_point:
  black_start = 0
  white_start = 0
  # 시작점을 기준으로 8*8로 보드를 자름
  for line_i,line in enumerate(board[start_m:start_m + 8]):
    for i, e in enumerate(line[start_n:start_n + 8]):
      # 검은색, 흰색으로 시작 경우의 수 모두 구함
      black_start += check_line(line_i, i, e, "B")
      white_start += check_line(line_i, i, e, "W")
  result.extend([black_start, white_start])
  
print(min(result))