#we are going to guess numbers
#computer generates

import random
random_number = random.randint(0,100)
guess = False
attempt = 0
max_attempt = 7
my_number = '0'
while my_number != random_number:
    print("Your mumber: ")
    my_number = int(input())
    attempt+=1
    if my_number == random_number:
        print("Congratulation! You've guessed the number from the", attempt, "attemp")
    else:
        if my_number > random_number:
            print("Choose smaller number") 
        else:
            print("Choose bigger number")
    if attempt >= 7:
        print("Sorry! You have no more attempts")  
        break          
#dac kommunikat"witaj w grze, jak ta gra dziala"
while (not guess) and (num_prob < 7):
    uzyt_zgaduje = input('Podaj liczbe: ')
    uzyt_zgaduje = int(uzyt_zgaduje)
    if uzyt_zgaduje == losowa_liczba
kommunikat
zmienic:zgadniete
zmienic:ilosx num_prob
kimmonikat: statystyki(zgadles w 5 probie...)