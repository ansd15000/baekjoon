import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    avg = sum(a[1:]) / a[0]
    cnt = 0
    for i in a[1:]:
        if i > avg: cnt += 1
    
    result = cnt / a[0] * 100
    # print(f'{result : .3f}%')  # 얘는 뭐 .. 출력시 앞자리가 띄어쓰기되서 나옴;
    print('{:.3f}%'.format(result))
'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''