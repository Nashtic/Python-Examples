from random import seed
from random import randint

#create a wanted number
wantedNumber = randint(0, 100)

#this function is our guessing function
def guessNumber():

    #we need to turn input to int input
    guessedNumber = int(input("Guess the number: "))

    #these are the comparisons
    if guessedNumber<wantedNumber:
        
        print("Your number is lower than wanted number")
        
        return guessNumber()

    elif guessedNumber>wantedNumber:

        print("Your number is higher than wanted number")

        return guessNumber()

    elif guessedNumber == wantedNumber:

        print("You find the wanted number! Congrats!")
        return 0


print("Take a number in your mind")

guessNumber()