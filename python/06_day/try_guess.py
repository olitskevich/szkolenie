import random
random_number = random.randint(0,100)
attempt = 0
max_attempt = 7
my_number = 555
try:
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
        if attempt >= max_attempt:
            print("Sorry! You have no more attempts, the correct number is", random_number)  
            break          
except KeyboardInterrupt:
    print ("Thanks for participation")