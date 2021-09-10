from random import randint
chance = 1
number = randint(1,10)
guess = int(input("guess the number between 1 to 10: "))
while guess != number:
    if guess < number:
        print("you guess is to lwo ")
        guess = int(input("guess the number again: "))
        chance = chance+1
    elif guess > number:
        print("you guess is to heigh ")
        guess = int(input("guess the number again: "))
        chance = chance+1
print()
print("congratulation you win")
print("number of cchances you took ", chance, "guess" )
