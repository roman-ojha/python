import random
print("\t\tSnake - Water - Gun")
print("\t------------------------------------")
print("Choose one of the flowing and Enter what you want to choose:")

i = 0
while (True):
    while (True):
        print("For: Snake Enter s:")
        print("For: Water Enter w:")
        print("For: Gun Enter g:")
        print("Enter here: ", end="")
        getdata = input()
        if getdata == "s":
            i = 1
            break
        elif getdata == "w":
            i = 2
            break
        elif getdata == "g":
            i = 3
            break
        else:
            print("\nInvalid letter !!!\nPlease Enter Again\n")
            continue
    varlist = [1, 2, 3]
    ran_generator = random.choice(varlist)
    if i == 1 and ran_generator == 2:
        print("\nyou choose Snake!!")
        print("opponent choose Water!!\n")
        print("you won!!!!!\tヽ(•‿•)ノ\n")
        print("Do you Want to play again:\nEnter 1 for Yes\nEnter 0 for NO:")
        play_Again = int(input())
        if play_Again == 1:
            continue
        elif play_Again == 0:
            break
        else:
            print("Invalid Number!!!")
            break
    elif i == 1 and ran_generator == 3:
        print("\nyou choose Snake!!")
        print("opponent choose Gun!!\n")
        print("you loose!!!!!\t(▰˘︹˘▰)\n")
        print("Do you Want to play again:\nEnter 1 for Yes\nEnter 0 for NO:")
        play_Again = int(input())
        if play_Again == 1:
            continue
        elif play_Again == 0:
            break
        else:
            print("Invalid Number!!!")
            break
    elif i == 2 and ran_generator == 1:
        print("\nyou choose Water!!")
        print("opponent choose Snake!!\n")
        print("you loose!!!!!\t(▰˘︹˘▰)\n")
        print("Do you Want to play again:\nEnter 1 for Yes\nEnter 0 for NO:")
        play_Again = int(input())
        if play_Again == 1:
            continue
        elif play_Again == 0:
            break
        else:
            print("Invalid Number!!!")
            break
    elif i == 2 and ran_generator == 3:
        print("\nyou choose Water!!")
        print("opponent choose Gun!!\n")
        print("you won!!!!!\n\tヽ(•‿•)ノ\n")
        print("Do you Want to play again:\nEnter 1 for Yes\nEnter 0 for NO:")
        play_Again = int(input())
        if play_Again == 1:
            continue
        elif play_Again == 0:
            break
        else:
            print("Invalid Number!!!")
            break
    elif i == 3 and ran_generator == 1:
        print("\nyou choose Gun!!")
        print("opponent choose Snake!!\n")
        print("you won!!!!!\n\tヽ(•‿•)ノ\n")
        print("Do you Want to play again:\nEnter 1 for Yes\nEnter 0 for NO:")
        play_Again = int(input())
        if play_Again == 1:
            continue
        elif play_Again == 0:
            break
        else:
            print("Invalid Number!!!")
            break
    elif i == 3 and ran_generator == 2:
        print("\nyou choose Gun!!")
        print("opponent choose Water!!\n")
        print("you loose!!!!!\n\t(▰˘︹˘▰)\n")
        print("Do you Want to play again:\nEnter 1 for Yes\nEnter 0 for NO:")
        play_Again = int(input())
        if play_Again == 1:
            continue
        elif play_Again == 0:
            break
        else:
            print("Invalid Number!!!")
            break
    else:
        print("\noohhhhh!!! Tie")
        print("You and oppnent choose same\n")
        print("Do you Want to play again:\nEnter 1 for Yes\nEnter 0 for NO:")
        play_Again = int(input())
        if play_Again == 1:
            continue
        elif play_Again == 0:
            break
        else:
            print("Invalid Number!!!")
            break
