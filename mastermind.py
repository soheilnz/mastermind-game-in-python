import random

def RandomNumbers(MaxRange):
    numbers = []
    for i in range(4):
        numbers.append(random.randint(1,MaxRange))
    return numbers

masterMind_list = RandomNumbers(MaxRange=5)
print(masterMind_list)
print("Welcome to Mastermind game!")
print("try to guess four secret numbers.\n")
print("you have 8 tries so be carefull!")

correct = 0
tries = 0

while correct < 4:
    guess1 = int(input("let's start dude! Please guess the first number: "))
    guess2 = int(input("Please guess the second number: "))
    guess3 = int(input("Please guess the third number: "))
    guess4 = int(input("Please guess the fourth number: "))
    tries += 1

    if guess1 == masterMind_list[0]:
        correct += 1
    if guess2 == masterMind_list[1]:
        correct +=1
    if guess3 == masterMind_list[2]:
        correct +=1
    if guess4 == masterMind_list[3]:
        correct +=1
    if correct < 4:
        if tries ==8:
            print("Nooo! you lose mate you use all your tries.\n maybe next time you can win this game.see you!")
            break
        else:
            print(f"you guest {correct} numbers correct")
            correct = 0
            continue
    else:
        if tries == 1:
            print(f" you win mate!\n you try {tries} time to win this round.")
            break
        else:
            print(f" you win mate!\n you try {tries} times to win this round.")
            break