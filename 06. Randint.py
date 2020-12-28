from random import randint as rint

computer_number = rint(0,100)
isGuessed = False
input("Hello, Let's play the game guess the number ")

while isGuessed != True:
    answer = int(input("Guess the number "))
    if answer == computer_number:
        print('Well done')
        isGuessed = True
    elif answer > computer_number:
        print('Много')
    else:
        print('Мало')
