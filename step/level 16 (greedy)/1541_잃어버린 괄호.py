# 진짜 어이없네. 런타임에러 왜뜨냐고
# a = '55-50+40+20-4+66-10+30+100'
# # a = '55-50+40'
# # a = input()
# l = list() # - location
# loc = -1
# while True:
#     loc = a.find('-',loc + 1)
#     if loc == -1 : break
#     else: l.append(loc)

# if len(l) <= 1: 
#     print(eval(a.replace('-','-(') + ')'))
# else: # 아니면 다음 마이너스까지 계산
#     print(eval( '(' + a.replace('-',')-(') + ')'))

# 코드 축약은 이래해도 되네.
# a = input()
# l = a.split('-')
# l = list(map(lambda x: str(eval(x)), l))
# print(eval('-'.join(l)))

# 숫자가 0으로 시작할 수 있다는게.. 01 09 이딴거였음
# 너무 바보처럼 짠거같은데.. ㅋㅋ
a = input().split('-')
l = [list(map(int, i.split('+'))) for i in a]
for i,v in enumerate(l):
    if len(v) > 1 : l[i] = [str(sum(map(int, l[i])))]  # 0으로 시작되는 문자형 숫자 제거를 위해 int변환후 연산후 문자변환
    else : l[i] = [str(sum(map(int, l[i])))]           # 마찬가지로 int -> str
l = sum(l, []) # 2차원을 1차원으로
print(eval('-'.join(l)))



# 55-50+40-10+30+100
# 55-50+40-(10+30+100)
# 55-(50+40)-10+30+100
# 55-50+40+20-4+66-10+30+100
# 55-50+40+20-4(+66-10+30+100) 이건 안된다 다행;

