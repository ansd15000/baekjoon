import sys
a = sys.stdin.readline().rstrip()
asc = [chr(i) for i in range(97, 123)]
for i, v in enumerate(asc):
    try:
        print(a.index(v), end= ' ')
    except:
        print(-1, end= ' ')

''' 
baekjoon
'''