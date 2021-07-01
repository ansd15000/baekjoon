# 당연하게도 시간초과...
# N = int(input())
# a = sorted([list(map(int, input().split())) for _ in range(N)])
# b = list()
# for i, v in enumerate(a):
#     a[i] = v[0]     # 회의 시작
#     b.append(v[1])  # 회의 끝

# result = 1      # 회의실 사용횟수
# __result = 1    # 순회하며 책정한 사용횟수
# i = 0           # 1씩 증가하는 시작시간 인덱스
# idx = 0         # 끝나는 시간 이후에 시작하는 시간의 배열 인덱스

# def findEndTimeIdx(l:list, val:int) -> int:
#     a = 0
#     if val in l:
#         # print(f'val: {val} l.index(val): {l.index(val)}')
#         return l.index(val) # 중복 시작시간은 문제가 생길 수 있음
#     else:
#         for i in range(len(l)-1, -1, -1):
#             if i == len(l)-1 and l[i] < val : 
#                 return -1
#             elif l[i] < val: 
#                 # print(f'jaegi. val: {val}')
#                 a = findEndTimeIdx(l, val+1)
#                 break
#         return a

# while i < int(len(a)): # 시작시간이 뒤인 에들은 필요없으니
#     idx = findEndTimeIdx(a, b[idx])
#     if idx != -1: 
#         __result +=1
#     else : # -1이면
#         # print(f'======={i}========')
#         # print(f'f: {i}, __result: {__result}, result: {result}')
#         if __result > result:
#             result = __result
#         __result = 1
#         i+=1
#         idx = i 
# print(result)

# 회의가 끝나야 진입이 가능함. 즉, 끝나는시간으로 정렬해서 순회를 돌며 가장 이전의 끝나는 시간보다 큰 시작시간을 체크해 개수를 세주면 됨
n = int(input())
l = list()
for i in range(n):
    a, b = sorted(map(int, input().split()))
    l.append(a, b)
l = sorted(l, key = lambda x: x[1]) # 끝나는 시간 기준으로 정렬
last = 0
cnt = 0
for i, j in l:      # 2차원 리스트는 그냥 이렇게 조질수있구나
    if i >= last:
        cnt += 1
        last = j
print(cnt)

'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''

