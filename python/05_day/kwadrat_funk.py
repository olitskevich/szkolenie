def funct_kwadr (a, b, c):
    d = b**2-4*a*c
    if d < 0:
        return False
    elif d == 0:
        x0 = -b/(2*a)
        return x0
    elif d > 0:
        x1 = (-b-d**0.5)/(2*a)
        x2 = (-b+d**0.5)/(2*a)
    return x1,x2
wartosc = funct_kwadr(1,2,1)
print(wartosc)
