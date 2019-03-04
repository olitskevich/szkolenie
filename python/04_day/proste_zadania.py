#wypisz liczby od 1 do 100, ale jak dziela sie na 3 --"Fizz, 5 --"Buzz"", 15--"FizzBuzz"

for number in range (1,101):
    pass
    if number % 15 == 0:
        print(str(number) + " FizzBuzz")
    elif number % 3 == 0:
        print(str(number) + " Fizz")
    elif number % 5 == 0:
        print(str(number) + " Buzz")
