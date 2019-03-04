# stworzyć funkcję, która jako argument przyjmuje tekst, 
# a zwraca słownik ze zliczonymi wystąpieniami literek w tym tekście

#oblicz wystąpienia literek w tekście. Użyj słownika.

#Co zrobić w kodzie:
#1. tworzycie tekst (dane wejściowe)
#2. tworzycie pusty słownik wystąpień dla literek (wystapienia = dict())
#3. pętla w której to obsługujecie
#4. print(wystapienia) żeby zobaczyć wyniki

#Dlaczego słownik?
#Bo jeżeli wystąpi literka 'a' 10 razy, to w naszym słowniku będzie:
#slownik['a'] == 10

#Wskazówka: Jak sprawdzić, czy dany klucz jest w słowniku?
#if klucz in slownik:

text = "carramba"
sl_wystapienie = {}



counter = 0

for letter in text:
    sl_wystapienie[letter] = 0

for key in sl_wystapienie:
    
    for letter in text:
        if key == letter:
            counter += 1
            sl_wystapienie[key] = counter
        else:
            counter -= 1
                       
print (sl_wystapienie)
