from sys import stdin
# 입력한 문자열이 아무리 숫자래도 정렬시 제대로 안되는 경향이 있는듯
# a = sorted([list(stdin.readline().split()) for _ in range(int(input())) ], key= lambda x: int(x[0]))
# for i, j in a:
#     print(int(i),j)

a = []
for _ in range(int(input())):
    age, name = stdin.readline().split()
    a.append([int(age),name])
a.sort(key= lambda x: x[0])
for i, j in a:
    print(i, j)
