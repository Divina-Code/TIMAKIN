computer_number = 35
isGuessed = False
input("Hello, Let's play the game guess the number ")

while isGuessed != True:
    answer = int(input("Guess the number"))
    if answer == computer_number:
        print('Well done')
        isGuessed = True
    elif answer > computer_number:
        print('Try again')
    else:
        print('Almost...')
