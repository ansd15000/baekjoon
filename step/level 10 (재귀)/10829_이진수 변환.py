n = int(input())
# print(f'{n:b}') # convert binary

l = []
def z(n):
    l.append(n % 2)
    a = int(n / 2)
    if a != 0:
        z(a)
    return l
print(''.join(map(str,(reversed(z(n))))))

