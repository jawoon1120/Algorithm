import sys

n = int(sys.stdin.readline())
input = [ tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
result = sorted(input, key=lambda x: (x[0], x[1]))
[print(*e) for e in result]