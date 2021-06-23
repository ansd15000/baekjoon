import sys

a = sys.stdin.readline().rstrip()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0
for i in croatia:
    if a.find(i) != -1:         # 크로아티아 문자 찾아서 있으면
        cnt += a.count(i)       # 갯수 세고
        a = a.replace(i,'__')   # 다른값으로 잠시 바꾸고
print(cnt + len(a.replace('__',''))) # 나머지 문자열 개수 더하기
# nljj 조질때 replace로 그냥 없애버리면 nj가 되버려서 이상해짐 ㅋㅋ


