# a, b = map(int, input().split())
# for i in range(a, b + 1):
#     sosu = True
#     for j in range(2, i):
#         if i % j == 0 : 
#             sosu = False
#             break
#     if sosu: 
#         print(i)

# 배꼇어요...
def z(num):
    if num == 1:
        return False
    for i in range(2, int(num**.5) + 1):
        if num % i == 0: return False
    return True

a, b = map(int, input().split())

for i in range(a, b+ 1 ):
    if z(i):
        print(i)


# def prime_list(a, b):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * b
 
#     # n의 최대 약수가 sqrt(b) 이하이므로 i=sqrt(b)까지 검사
#     m = int(b ** 0.5)
#     for i in range(a, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우 
#             for j in range(i+i, b, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False
 
#     # 소수 목록 산출
#     return [i for i in range(a, b) if sieve[i] == True]

# a, b = map(int, input().split())
# print(prime_list(a, b))