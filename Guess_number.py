#Guess the number...
import random
target = random.randint(1,100);

while True:

    userChoice = (input("Enter the target number or quit(Q): "));
    if(userChoice == "Q"):
        break;
    userChoice = int(userChoice);

    if(userChoice == target):
        print("Success: Correct Guess!");
        break;
    elif(userChoice < target):
        print("You guessed the smaller number.Guess larger one");
    else:
        print("You guess the larger number.Guess smaller one...");
print("-----GAME OVER------")
