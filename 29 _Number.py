import random

def comp(value):
    comp_choice = random.randint(1, 5)
    print("computer chooses", comp_choice)
    for ele in range(value, value+comp_choice):
        if ele == 29:
            print("Computer lose")
            print("You won")
            exit(0)
        print(ele)
    return value+comp_choice

def user(value):
    user_choice = int(input("Enter a number between 1 and 5: "))
    if 1 <= user_choice <= 5:
        if user_choice == 1:
            print("Enter", value, "or you will be disqualified")
        else:
            print("Enter from", value, "to", (value+user_choice-1), "consecutively or you will be disqualified")
        for ele in range(value, value+user_choice):
            n = int(input())
            if n!=ele:
                print("You are Disqualified!!")
                exit(0)
            if n == 29:
                print("You lose")
                print("Computer won")
                exit(0)
    else:
        print("Wrong input!!\nTry again")
        user(value)
    return value+user_choice


def game():
    value = 1
    print("Press 1 for 1st turn")
    print("Press 2 for 2nd turn")
    choice = int(input("Enter your choice: "))
    while True:
        if choice == 1:
            value = user(value)
            value = comp(value)
        else:
            value = comp(value)
            value = user(value)


game()