# counting sort
# 메모리(8mb) 초과...
# import sys
# n = int(input())
# a = [int(sys.stdin.readline()) for _ in range(n)]
# l = [0]* (max(a) + 1) # 인덱스가 요소값인 배열 선언. 최대길이는 그래서 가장 큰 값의 +1 이어야 인덱스가 알맞는다.

# for i in range(n): 
#     l[a[i]] += 1

# for i in range(len(l)):
#     for j in range(l[i]): # 해당 인덱스의 개수만큼 반복출력
#         print(i)

import sys
n = int(input())
l = [0]* 10001 # 입력받는 값중엔 10000 을 초과하진 않는다는 제약. 
# 만약 제약이 없다면 입력값중 최대값을 추적해야하는데 그 값이 10**16 처럼 졸라크면 메모리가 남아나질 않음. 이 때문에 메모리제약이 있는 문제로 출제됨

for i in range(n): 
    num = int(sys.stdin.readline()) # 입력값을 배열로 만들어 버리면 메모리초과되니 1:1 대응으로 추가시킴
    l[num] += 1

for i in range(len(l)):
    for j in range(l[i]): # 해당 인덱스의 개수만큼 반복출력
        print(i)
'''
10
5
2
3
1
4
2
3
5
1
7
'''