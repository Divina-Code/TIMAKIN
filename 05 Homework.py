isGuessed = False
input("Hello, Let's play the game guess the number ")
while isGuessed != True:
    answer = ("Guess the number")
    computer_number = input(answer)
    if computer_number == "35":
        print('Well done')
        isGuessed = True
    elif answer >= "35":
        print('Try again')
    else:
        print('Almost...')




