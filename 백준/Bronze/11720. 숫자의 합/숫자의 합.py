import sys

N = int(sys.stdin.readline())
num = sys.stdin.readline().rstrip()

sum = 0
for n in num:
    sum += int(n)
    
print(sum)