# 곱셉의 중간과정을 화면에 표기한다.
# 한줄입력이 아니라 엔터단위로 나뉘니까 이래 설정하자.
a, b = input(), input()
for i in b[::-1]: print(int(a) * int(i))
print(int(a) * int(b))