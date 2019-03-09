# stworzyć funkcję, która jako argument przyjmuje tekst, 
# a zwraca słownik ze zliczonymi wystąpieniami literek w tym tekście

def count_letters(tekst):
    #tekst="Ala ma kota, kot ma Ale"
    wystapienia=dict()

    for literka in tekst:
        if literka in wystapienia:
            wystapienia[literka] += 1
        else:
            wystapienia[literka]=1
    return wystapienia
print (count_letters("ile liter w tym zdaniu"))