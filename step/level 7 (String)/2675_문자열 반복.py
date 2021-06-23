import sys
T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    a, b = map(str, sys.stdin.readline().rstrip().split())
    print(''.join(map(lambda x: x * int(a), b)))  

'''
2
3 ABC
5 /HTP
'''