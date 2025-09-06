import random

def isNum(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def move(num):
    match num:
        case 0:
            return "Scissors"
        case 1:
            return "Rock"
        case 2:
            return "Paper"

while True:
    user = input("Enter your choice (0 for scissors, 1 for rock, 2 for paper):")
    
    if isNum(user) == False:
        print("You must write a number!! (0-2)")
        break
    elif int(user) < 0 or int(user) > 2:
        print("It must be 0, 1 or 2 only!!")
        break

    computer = random.randint(0, 2)

    print(f"Your choice: {move(int(user))}")
    print(f"Computer's choice: {move(computer)}")
    if int(user) == computer:
        print("Draw!")
    elif (user == 0 and computer == 2) or (user == 1 and computer == 0) or (user == 2 and computer == 1):
        print("You win!")
    else:
        print("You lose!")
    break
