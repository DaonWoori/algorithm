import sys

n = 1000
arr = [False, False] + [True] * (n-1) # 1000 이하의 자연수만 주어짐

prime = []
for i in range(2, n+1):
    if arr[i]:
        prime.append(i)
    for j in range(2*i, n+1, i):
        arr[j] = False 

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

count = 0
for n in nums:
    if n in prime:
        count += 1

print(count) 