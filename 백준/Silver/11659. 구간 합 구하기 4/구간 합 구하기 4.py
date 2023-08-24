import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] # 합 배열을 저장할 변수
temp = 0

# 합 배열 계산
for i in nums:
  temp += i
  prefix_sum.append(temp)

# 구간 합 계산
for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  print(prefix_sum[j] - prefix_sum[i-1])