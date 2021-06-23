import sys
a = sys.stdin.readline().rstrip()
a = a.upper()
maxvalue = 0
result = None
for i in set(a):
    v = a.count(i)
    if v >= maxvalue : # 가장많이 사용된거
        result = '?' if maxvalue == v else i
        maxvalue = v
print(result)
'''
Mississipi
===========
zZa
'''