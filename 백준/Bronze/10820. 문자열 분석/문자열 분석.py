import sys

while True:
  input = sys.stdin.readline()
  if not input:
    break
  result = [0]*4
  for c in input:
    if c.islower():
      result[0]+=1
    elif c.isupper():
      result[1]+=1
    elif c.isdecimal():
      result[2]+=1
    elif c==' ':
      result[3]+=1
  print(*result)