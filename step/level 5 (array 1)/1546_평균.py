import sys
N = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
M = max(a)
for i in range(N):
    a[i] = a[i] / M * 100 
print(sum(a)/N)