#wypisz liczby w zakresie od 1 do 100
 
first_num = [True] * 100
first_num[0] = False
first_num[1] = False

for num in range (2, 51):
    n = 2
    wielokrotnosc = num * n
    while wielokrotnosc < 100:
        first_num[wielokrotnosc] = False
        n += 1
        wielokrotnosc = n * num

for indeks, wartosc in enumerate(first_num):
    if wartosc == True:
        print("Liczba pierwsza: ", indeks)        


