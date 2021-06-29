# 너무어려워
# N = int(input()) # 전체 사각형 크기. 항상 3의 거듭제곱
# innerSquare = int(N / 3) # # 내부 사각형의 크기
# c = ['***', '* *', '***']
# blank = '   '
# # 딱 9 * 9 까지 가능
# def square(a):
#     interval = int(a / 3) if a >=9 else 1# 가운데 공백 
#     result = ''
#     print(f'interval: {interval}')
#     for i in range(a): # 한줄씩 출력합니다
#         if interval <= i < a - interval: # 중간 공백을 출력하는 부분.. /3 해도 될듯?
#             result += '\n'.join(map(lambda x : (x * interval) + (blank * interval) + (x * interval), c)) + '\n'
#         else : # 중간공백을 제외한 출력. 단, 패턴으로 출력되어야함.
#             # result += '\n'.join(map(lambda x : x * a, c)) + '\n' # 27 이상으로 하면 각 9 x 9  위치에 빈공간을 생성하는법을 알아야함      
#             result += '\n'.join(map(lambda x : x * a, c)) + '\n'
#             pass
    
#     return result.rstrip()

# def main():
#     innerSquare = int(N / 3)
#     result = ''
#     if innerSquare < 9 :
#         print(square(innerSquare))
#     else:
#         a = square(3) # 큰수의 최소 (가로세로 9)
#         interval = int(innerSquare / 3) # N이 27 기준 innersquare는 9, 이걸 3줄동안 출력
#         for _ in range(interval):
#             # if i == interval / 3:
#             #     pass
#             # else: 
#             #     print('\n'.join(map(lambda x: x*interval, a.split('\n'))))
#             result += '\n'.join(map(lambda x: x*interval, a.split('\n'))) + '\n'
#         result = result.rstrip().split('\n')
#         for i in range(innerSquare):
#             replacing = result[innerSquare + i] # 별이 있는 문자열
#             data = replacing[innerSquare: -innerSquare].replace('*',' ')
#             newdata = replacing[:innerSquare] + data + replacing[-innerSquare:]
#             result[innerSquare + i] = newdata
#         print('\n'.join(result))
#         return result
# main()

def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)] # *** 맨위 아래

def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    top_bottom = concatenate(x, x)
    middle = concatenate(x, [' '*n]*n)
    return top_bottom + middle + top_bottom

print('\n'.join(star10(int(input()))))