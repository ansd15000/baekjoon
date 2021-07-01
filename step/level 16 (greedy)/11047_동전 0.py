# while 쓰는게 좀 느리다. idx 감소 때문일까
N, a = map(int, input().split())
b = [ int(input()) for _ in range(N)] # 동전 종류
idx = len(b) -1 # 뒤에서부터 계산
result = 0      # 동전 갯수
while a != 0:
    if a // b[idx] > 0:
        result += a // b[idx]
        a %= b[idx]
    idx -= 1
print(result)


# for 쓰는게 더 빠르네 뭐지
# N, a = map(int, input().split())
# b = [ int(input()) for _ in range(N)] # 동전 종류
# result = 0                            # 동전 갯수
# for i in range(N -1, -1, -1):         # 뒤로 카운트 하는게 더 빠르대
#     if a == 0: break
    
#     if a // b[i] > 0:
#         result += a // b[i]
#         a %= b[i]
#         continue
# print(result)


# 시간초과.. ㅋㅋ 파이썬 짜증나네
# while a != 0:   # 0되면 끝
#     if a - b[idx] < 0:  # 동전교환시 음수가 되면 안돼
#         idx -=1
#         continue
#     else:
#         result += a // b[idx]
#         idx -=1

