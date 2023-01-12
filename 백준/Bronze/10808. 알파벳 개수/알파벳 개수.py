import sys
from collections import Counter
counter_input = Counter(sys.stdin.readline().strip())
result =[0]*26
for key in counter_input:
  result[ord(key)-97]=counter_input[key]
print(*result)