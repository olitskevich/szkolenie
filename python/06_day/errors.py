try:
    1/0
except ZeroDivisionError:
    print ("division by zero")


try:
    list = [1, 3, 6]
    list[5]
except IndexError:
    print ("list index out of range")

try:
    a = {'aa':'11', 'bb':'22'}
    a['abc']
except KeyError:
    print("abc")

try:
    list = [1, 3, 5]
    list.appent(5)
except AttributeError:
    print("'list' object has no attribute 'appent'")

try:
    num = 10
    num(10)
except TypeError:
    print("'int' object is not callable")

try:
    funct = ala(5)
except NameError:
    print("name 'a' is not defined")