#ASCII Rock, Paper, Scissors ASCII Art by wynand1004 from GitHub

from random import random
from random import randint


def rockPaperScissorsChoice():
    
    playerWinCount = 0
    computerWinCount = 0

    while(True):

        playerChoice = int(input("Rock, Paper or Scissors?\nRock: 1\nPaper: 2\nScissors: 3\n"))
        computerChoice = randint(1, 3)

        if playerChoice == 1 and computerChoice == 1:
            print("Rock x Rock = Draw")
            print("""
                 ________                   _______
            ---'     ____)      \    /     (____   '---   
                    (_____)      \  /     (_____)
                    (_____)       \/      (_____)
                    (____)        /\       (____)
            ---.____(___)        /  \       (___)__.---
            """)

            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)

            wannaPlay = input("Would like to play one more game? (yes/no)\n")
            
            if wannaPlay == 'no':
                break
            
        elif playerChoice == 1 and computerChoice == 2:
            print("Rock x Paper = Paper Wins!")
            print("""
                    ________                       _______
                ---'    ____)      \    /     ____(____  '---   
                       (_____)      \  /     (_____
                       (_____)       \/      (_____
                       (____)        /\       (____
                ---.___(___)        /  \        (_________.---
            """)

            computerWinCount = computerWinCount+1

            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)

            wannaPlay = input("Would like to play one more game? (yes/no)\n")
                
            if wannaPlay == 'no':
                break

        elif playerChoice == 1 and computerChoice == 3:
            print("Rock x Scissors = Rock Wins!")
            print("""
                 _______                        _______
            ---'    ____)       \    /     ____(____   '---   
                    (_____)      \  /     (_____
                    (_____)       \/     (_________
                    (____)        /\          (____)
              ---.__(___)        /  \          (___)__.---
            """)

            playerWinCount = playerWinCount+1

            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)
            
            wannaPlay = input("Would like to play one more game? (yes/no)\n")
            
            if wannaPlay == 'no':
                break

        elif playerChoice == 2 and computerChoice == 3:
            print("Paper x Scissors = Scissors Wins!")
            print("""
                 _______                           _______
             ---'   ____)____      \    /     ____(____   '---   
                        _____)      \  /     (_____
                        _____)       \/     (_________
                        ____)        /\          (____)
            ---.__________)         /  \          (___)__.---
            """)

            computerWinCount = computerWinCount+1

            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)

            wannaPlay = input("Would like to play one more game? (yes/no)\n")
            
            if wannaPlay == 'no':
                break

        elif playerChoice == 2 and computerChoice == 2:
            print("Paper x Paper = Draw!")
            print("""
                 _______                           _______
             ---'   ____)____      \    /     ____(____   '---   
                        _____)      \  /     (_____
                        _____)       \/      (_____
                        ____)        /\       (____
            ---.__________)         /  \        (_________.---
            """)


            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)

            wannaPlay = input("Would like to play one more game? (yes/no)\n")
            
            if wannaPlay == 'no':
                break

        elif playerChoice == 2 and computerChoice == 1:
            print("Paper x Rock = Paper Wins!")
            print("""
                ________                         _______
            ---'    ____)____      \    /       (____   '---   
                        _____)      \  /       (_____)
                        _____)       \/        (_____)
                        ____)        /\         (____)
            ---.__________)         /  \         (___)__.---
            """)

            playerWinCount = playerWinCount+1

            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)

            wannaPlay = input("Would like to play one more game? (yes/no)\n")
            
            if wannaPlay == 'no':
                break

        elif playerChoice == 3 and computerChoice == 1:
            print("Scissors x Rock = Rock Wins!")
            print("""
                 _______                       _______
             ---'   ____)____    \    /       (____   '---   
                        _____)    \  /       (_____)
                    __________)    \/        (_____)
                   (____)          /\         (____)
             ---.__(___)          /  \         (___)__.---
            """)

            computerWinCount = computerWinCount+1

            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)

            wannaPlay = input("Would like to play one more game? (yes/no)\n")
            
            if wannaPlay == 'no':
                break

        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors x Paper = Scissors Wins!")
            print("""
                 _______                          _______
             ---'   ____)____    \    /       ___(____   '---   
                        _____)    \  /       (____
                    __________)    \/        (_____
                   (____)          /\         (____
             ---.__(___)          /  \          (________.---
            """)

            playerWinCount = playerWinCount+1

            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)

            wannaPlay = input("Would like to play one more game? (yes/no)\n")
            
            if wannaPlay == 'no':
                break

        elif playerChoice == 3 and computerChoice == 3:
            print("Scissors x Scissors = Draw")
            print("""
                 _______                           _______
             ---'   ____)____    \    /      _____(____   '---   
                        _____)    \  /      (_____
                    __________)    \/      (___________ 
                   (____)          /\            (____)
             ---.__(___)          /  \            (___)___.---
            """)

            print("Player Total Wins: ", playerWinCount)
            print("Computer Total Wins: ", computerWinCount)

            wannaPlay = input("Would like to play one more game? (yes/no)\n")
            
            if wannaPlay == 'no':
                break


rockPaperScissorsChoice()