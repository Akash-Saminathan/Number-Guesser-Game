import random
while True:
    a = int(input("Enter start value: "))
    b = int(input("Enter end value: "))
    randomval = random.randint(a,b)
    finalcondition = 0
    while True:
        guessval = int(input(f"Guess the number between {a} and {b}: "))
        if guessval==randomval:
            print("You guessed correctly!\n")
            condition = input("Would you like to play again?(y/n): ")
            if condition=="y":
                finalcondition = "y"
                break
            else:
                break
        else:
            condition = input("Wrong answer, would you like to try again?(y/n): ")
            if condition=="y":
                continue
            else:
                break
    if finalcondition=="y":
        continue
    else:
        break

    
