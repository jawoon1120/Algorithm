import sys
n = int(input())

# 문장을 2차원 배열로 할당 문장 - 단어
case = [sys.stdin.readline().strip().split() for _ in range(n)]

line = []
for words in case:
  reversed_words = [word[::-1] for word in words]
  line.append(' '.join(reversed_words))

[print(l) for l in line]