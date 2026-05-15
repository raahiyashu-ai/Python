import random 
playing=True
number=str(random.randint(0,9))
print("I will print numbers from 0 to 9. You shoud guess the number one digit at a time.")
print("The game ends when you guess yhe wrong number!!!! ")
while playing:
    guess=input("Give me your best guess!!!\n")
    if number == guess:
        print("You win the game !")
        break
    else:
        print("Your guess was wrong please try again.\n")
        print("The number was",number)