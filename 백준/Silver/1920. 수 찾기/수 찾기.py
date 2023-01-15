import sys
from collections import defaultdict

counter = defaultdict(int)
_ = sys.stdin.readline()
for an in sys.stdin.readline().split():
  counter[an] = 1
_ = sys.stdin.readline()
[print(counter[am]) for am in sys.stdin.readline().split()]