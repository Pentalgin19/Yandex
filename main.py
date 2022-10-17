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
            if b > c:
                b, c = c, b
            if c > d:
                c, d = d, c
            if b > d:
                b, d = d, b
            a, b, c, d = b, a, c, d
else:
    a, b, c, d = a, b, c, d
print(str(a) + str(b) + str(c) + str(d))
