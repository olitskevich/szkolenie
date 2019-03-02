uczestnik = "Tomek"
dziennik =["Olga", "Tomek", "Piotr"]

for pozycja, uczen in enumerate(dziennik):
    #pass print(pozycja, ":", uczen)

    if uczen == uczestnik:
        print(pozycja, ":", uczen)

#if uczestnik in dziennik:
#    print("Znalazlam") 