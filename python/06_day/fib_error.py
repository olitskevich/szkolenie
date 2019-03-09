def fibonacci(m):
    #wymagania m:
    #1. number
    #2. number >=2
    if not isinstance(m, int):
        raise Exception ("It is not int. Please, enter integer!")
    if m < 2:
        raise Exception ("Please, enter a number bigger than 1!")
    lista = [0, 1]
    for liczba in range(2, m+1):
        lista.append(lista[liczba-1]+lista[liczba-2])
    return lista[m]

try:
    print(fibonacci(-8))
except Exception as exc:
    print ("Try again!")
    print(exc.args[0])l