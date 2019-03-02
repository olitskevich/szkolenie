#Sprawdz czy zadany tekst jest palindromem

text = "piotrrtoiX"
if_palindrome = True 
for position, letter in enumerate(text):
    if text[position] == text[-position - 1]:
        continue
    else:
        if_palindrome = False  
        break 

if if_palindrome:
    print("It is a Polindrome")
else:
    print("It is NOT a Polindrome")