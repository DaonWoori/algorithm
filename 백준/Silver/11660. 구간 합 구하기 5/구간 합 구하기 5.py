import sys

N, M = map(int, sys.stdin.readline().split())

# 주어지는 2차원 배열 -> 0번째 항을 0으로 채움
A = [[0] * (N + 1)]

# 구간 합 배열을 저장하는 배열 -> 모든 값을 0으로 채움
P = [[0] * (N + 1) for _ in range(N+1)]

# 배열 입력 받기
for _ in range(N):
  nums = list(map(int, sys.stdin.readline().split()))
  A_row = [0] + nums
  A.append(A_row)


# 합 배열 계산
for i in range(1, N+1):
  for j in range(1, N+1):
    P[i][j] = P[i][j-1] + P[i-1][j] - P[i-1][j-1] + A[i][j]

# 구간 합 계산하기
for _ in range(M):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

  result = P[x2][y2] - P[x1-1][y2] - P[x2][y1-1] + P[x1-1][y1-1]
  print(result)
    