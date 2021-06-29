a = int(input()) #전체 사각형 크기 
b = int(a / 3) # 사각형 가로세로길이. 가운데 공백 있어야함
c = ['***', '* *', '***']
d = ['   ']
# c = ['***', '* *', '***']
# res = None
# for i in range(b):
#     res+=c

def n_start(size):
    result = ''
    for i in range(int(size / 3)): # 만약 9면 3으로
        if int(size / 2) == i : # 비어있어야 할 중간부분일 경우
            result += d + '\n'
            print(d + '\n')
        else:
            print((c * size) + '\n') 
            result += (c * size) + '\n'
    return result

print(n_start(b))

# 1
# 1-1 싸이클은 걍 곱셈
# 1-2 싸이클은 b / 3 / 2 위치에 빈값 넣고
# 1-3 싸이클은 처음과 동일

# 2
# 2-1 싸이클은 0~9, 9~19, 18 ~ 28 순서대로 곱, 공백 곱
# 2-2 싸이클은
# 2-3 싸이클은

# 3
# 1 사이클과 동일