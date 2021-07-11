# 시간초과 ㅋㅋ 참나
# print( '\n'.join(map(str, reversed([int(input()) for _ in range(int(input()))]))) )

# 삽입정렬도 불가능. 내장함수도 안되는데 당연한거지..
# n = int(input())
# a = [int(input()) for _ in range(n)]
# # 삽입정렬은 맨 앞자리가 이미 정렬되있어야함
# for i in range(1, n):
#     for j in range(i, 0, -1):
#         if a[j-1] > a[j] : 
#             a[j-1], a[j] = a[j], a[j-1]
# print('\n'.join(map(str,a)))


# 컨프리헨션 백준에서 틀렸다고 하는거 개빡치네
# print( '\n'.join(map(str, [int(sys.stdin.readline()) for _ in range(int( sys.stdin.readline()))])) ) 
import sys # 입력데이터 많은경우 input 으로 하면 시간초과 나는거.. sys로 처리하면 해결됨..
n = int( sys.stdin.readline() )
a = []
for _ in range(n):
    a.append( int(sys.stdin.readline()) )
print('\n'.join(map(str, sorted(a))))
# print(a)

'''
5
5
4
3
2
1
'''