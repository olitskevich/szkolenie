#stworzyć funkcję przyjmującą argument "m" i obliczającą m-ty wyraz ciągu Fibonacciego

def fibonacci(m):
    lista = [0, 1]

    for liczba in range(2, m+1):
        lista.append(lista[liczba-1]+lista[liczba-2])

    return lista[m]
#print(lista, m,"-ty element to:", lista[m])

#return lista[m]
wartosc = fibonacci(6)
wartosc2 = fibonacci(2)
print("m-ty element:", wartosc)
#print("m-ty element: ",fibonacci(6))