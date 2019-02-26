#!/usr/bin/env python

zmienna1 = 1
zmienna2 = 'text'
zmienna3 = True
zmienna4 = []
zmienna5 = 3.14
zmienna6 = None

print(zmienna1)
print(zmienna2)
print(zmienna3)
print(zmienna4)
print(zmienna5)
print(zmienna6)

#PEP8
if zmienna1 == 3:
    # esli WARUNEK jest spelniony
    print (3)
elif zmienna1 == 4:    
    # esli INNY_WARUNEK jest spelniony
    print(4)
elif zmienna1 == 'blabla':
    print('blabla')
elif zmienna1 == 9:
    print('1')        
else:
    # instrukcja jesli zaden z powyzszych nie jest spelniony
    print ('nie ma takiej zmiennej')
