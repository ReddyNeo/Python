import random
n = 20
to_be_guessed = int(n * random.random()) + 1
guess = 0
while guess != to_be_guessed:
    guess = int(input("Enter Number : "))
    if guess > 0:
        if guess > to_be_guessed:
            print("Number is too large")
        elif guess < to_be_guessed:
            print("Number is too small")
    else:
        print("Sorry that your give up ! ")
        break
else:
    print("Congratulation , You made it !")
