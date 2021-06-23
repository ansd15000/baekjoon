# reversed는 reversed 객체로 리스트나 튜플로 반환함.
import sys
a,b  = map(lambda x : ''.join(reversed(x)), sys.stdin.readline().split())
if int(a) > int(b): print(a)
else : print(b)