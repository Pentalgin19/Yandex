x = int(input())
a = (x - x % 1000) // 1000
b = (x - x % 100) // 100 % 10
c = (x - x % 10) // 10 % 10
d = x % 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a == 0:
    if b == 0:
        if c == 0:
            if d == 0:
                print('0000')
            else:
                a, b, c, d = d, a, b, c
        else:
            if d == 0:
                a, b, c, d = c, a, b, d
            else:
                a, b, c, d = min(c, d), a, b, max(c, d)
    elif c == 0:
        if d == 0:
            a, b, c, d = b, a, c, d
        else:
            m = min(b, d)
            a, b, c, d = m, a, c, max(b, d)
    else:
        if d == 0:
            a, b, c, d = min(b, c), a, d, max(b, c)
        else:
            if d != max(d, b, c) and d != min(d, b, c):
                a, b, c, d = min(b, c, d), a, d, max(d, b, c)
            elif b != max(d, b, c) and b != min(d, b, c):
                a, b, c, d = min(b, c, d), a, b, max(d, b, c)
            elif c != max(d, b, c) and c != min(d, b, c):
                a, b, c, d = min(b, c, d), a, c, max(d, b, c)
else:
    a, b, c, d = a, b, c, d







# if a == 0:
#     m = min(b, c, d)
#     a = m
# if b == 0:
#     m = min(a, c, d)
#     b = m
# if c == 0:
#     m = min(b, a, d)
#     c = m
# if d == 0:
#     m = min(b, c, a)
#     d = m
print(str(a) + str(b) + str(c) + str(d))
































