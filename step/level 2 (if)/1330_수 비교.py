# 제한사항이 있어서 추가했는데 이건 안쓰나봄
a, b = map(int, input().split())

# if -10000 <= a <= 10000 : raise('error')
# if -10000 <= b <= 10000 : raise('error')

if a > b : print('>')
elif a < b : print('<')
elif a == b : print('==')