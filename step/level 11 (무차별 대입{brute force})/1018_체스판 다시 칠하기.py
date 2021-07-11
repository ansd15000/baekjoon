# # 8*8 체스판 추출하기
m, n = map(int, input().split())
a = [input() for _ in range(m)]
print()

# 왜틀림
# res = None
# for i in range(m-7):             # 세로줄 8개씩 더 탐색할 반복수
#     for k in range(n -7):        # 가로줄 8개씩 더 탐색할 반복수
#         # print(f'k: {a[j][k:]}', end = ' ')
#         # print(f'k: {k}')
#         pat = {0: 'W', 1:'B'} if a[i][0] == 'W' else {0: 'B', 1:'W'} # 여기가 재선언 되는 문제를 막아야함
#         # print(f'start: {k}, {i}')
#         temp = 0
#         for j in range(i, 8 + i):       # 세로줄 탐색 시작수
#             # print(f'j: {j}')
#             # print(a[j])
#             t1 = []
#             cnt = 0
#             for l in range(k, 8+k): # 가로줄 탐색 시작인덱스
#                 # print(f'l: {l}')
#                 # print(a[j][l], end='')
#                 # print(pat[l % 2], end='')
#                 t1.append(pat[cnt % 2])
#                 if a[j][l] != pat[cnt % 2]:
#                     temp+=1
#                 cnt +=1
#             # print()
#             # print(''.join(t1))
#             # print(temp)
#             pat[0], pat[1] = pat[1], pat[0]
#         # print('----------------')
#         # print(f'temp: {temp}, res: {res}')
#         if res is None : res = temp
#         elif res > temp : res = temp
#     # print('=============\n')
# print(res)

# 결국 풀이를 봤습니다........
z = []
for i in range(m-7):             # 세로줄 8개씩 더 탐색할 반복수
    for k in range(n -7):        # 가로줄 8개씩 더 탐색할 반복수
        w , b = 0, 0             # w로 시작할때랑 b로 시작할때 칠해야할부분 
        for j in range(i, 8 + i):   # 세로줄 탐색 시작수
            for l in range(k, 8+k): # 가로줄 탐색 시작인덱스
                if (j + l) % 2 == 0 : # 시작위치 다음부터의 홀짝순서를 정할 수 있음.. 0,0 0,1 0,2  ... 1,0 1,1 1,2  각위치를 더하면 짝홀짝, 홀짝홀 이래되니
                    if a[j][l] == 'W': w +=1    # 짝수가 W로 시작했다면
                    else: b+=1 # B로시작했음
                else:
                    if a[j][l] == 'B': w +=1    # 홀수는 B일때 세줘야함
                    else: b+=1 # 홀수가 W일때 계산.
        z.append(w)
        z.append(b)

print(min(z)) # 즉, 이 배열은 w,b 중 어느 하나로 시작했을 모든 경우를 담아두는 배열임. 그러니 최소값만 구하면 되겠네
    # print('=============\n')
    # print(z)
# print(res)