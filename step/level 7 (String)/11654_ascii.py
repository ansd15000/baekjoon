import sys

a = sys.stdin.readline().rstrip()
if str(type(a)) == "<class 'str'>":
    print(ord(a))
elif str(type(a)) == "<class 'int'>":
    print(chr(a))