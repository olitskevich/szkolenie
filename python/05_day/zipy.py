#Napisz funkcje, ktora liczy srednia wazona. Przyjmuje 2 argumenty:
#*wartosci
#*wagi


def sr_wazona(wartosci, wagi):
    licznik = 0
    mianownik = 1 
    for wartosc, waga in zip(wartosci, wagi):
        licznik = wartosc * waga + licznik
        mianownik = waga + mianownik
    return licznik / mianownik
war = sr_wazona([3,6], [1,2])
print (war)


