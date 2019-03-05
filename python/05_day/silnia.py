def silnia(n):
    list = [1, 2]
    for number in range(2, n+1):
        print(number)
        list.append(list[number-1]*list[number-2])
    return list[number]
wartosc = silnia(4)        
print(list)

