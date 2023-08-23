import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

sum = 0

max_score = max(scores)

for s in scores:
  sum += (s / max_score * 100)

print(sum / N)