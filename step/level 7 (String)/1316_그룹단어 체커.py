import sys
T = int(sys.stdin.readline().rstrip())
cnt = 0
for _ in range(T):
    a = sys.stdin.readline().rstrip()
    s = sorted(set(a))  # 연속값 체크를 위한 요소모음
    groupText = True
    for i in s:
        z = a.rindex(i) # 마지막으로 발견된 단어의 위치
        if len(set(a[a.index(i): z + 1])) != 1: # set이기에 연속됐다면 길이가 1 이상이 나오면 안됨
            groupText = False
            break
    if groupText: cnt += 1
print(cnt)
# 개쩔었다 ㅋㅋ 라고할뻔.


'''
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)

# sorted로 정렬조건으로 find 를 하면... 리스트 앞에서부터 같은 요소를 앞으로 당겨옴..
# 세상에 똑똑한 사람들 진짜 많다!! 젠장
'''

'''
4
aba
abab
abcabc
a
'''