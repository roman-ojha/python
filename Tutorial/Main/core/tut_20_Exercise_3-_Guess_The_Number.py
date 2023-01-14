num = 18
while(True):
    print("Guess the number:", end=" ")
    number = input()
    if int(number) > num:
        print("Number is lesser then what you have entered")
        print("try it again")
        continue
    if int(number) < num:
        print("Number is greater then what you have entered")
        print("try it again")
        continue
    else:
        print("yoooo! you guess it write the number is 18")
        break
