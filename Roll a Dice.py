import random

option = input("Enter Y to roll the dice\nEnter N to exit: ")

if (option == "y" or option == "Y"):
    no = random.randint(1,6)
    if(no == 1):
        print("[---]\n[   ]\n[ 0 ]\n[   ]\n[---]")
    if(no == 2):
        print("[---]\n[ 0 ]\n[   ]\n[ 0 ]\n[---]")
    if(no == 3):
        print("[---]\n[   ]\n[000]\n[   ]\n[---]")
    if(no == 4):
        print("[---]\n[0 0]\n[   ]\n[0 0]\n[---]")
    if(no == 5):
        print("[---]\n[0 0]\n[ 0 ]\n[0 0]\n[---]")
    if(no == 6):
        print("[---]\n[0 0]\n[0 0]\n[0 0]\n[---]")
else: 
    print("Game Ended.")

