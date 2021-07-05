# 약수 패턴은 맨 처음과 맨 끝 곱하면 원래 수가 나옴.
# 근데 입력값이 정렬 안되있는건 모르고있었네 아 ㅋㅋ;
n = int(input())
a = sorted((map(int, input().split())))
print(a[0] * a[-1])    