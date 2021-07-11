from sys import stdin
a =[list(map(int, stdin.readline().split())) for _ in range(int(stdin.readline()))]
a.sort(key = lambda x: [x[1], x[0]])
for i, j in a:
    print(i, j)

# key 인자는 기준값을 말한다. 람다 인자값에 x[0] 을 주면 그 위치 값 기준으로 전체정렬을 하는데, 두번째 인자값도 정렬기준을 하려면 컴마기준 x[1] 이래주면 됨.
# 이때 두번째 정렬기준은 내림차순으로 하고싶다면 앞에 - 를 붙힌다. ex) sorted(a, key = lambda x : [x[0], -x[1]]) 이런식으로
'''
6
0 4
1 2
1 -1
-1 -1
2 2
3 3
'''