from time import sleep
from random import randint as rint
playcard = rint(2, 11)
player1 = rint(2,11)
player2 = rint(2,11)
print("Player1, your score is", player1)
print("Player2, your score is", player2)

inGame1 = True
inGame2 = True

while  inGame1 or inGame2:


     if inGame1:
          take_card = input("Будешь брать карту?[ДА/НЕТ]")
          if take_card == "ДА":
               player1 += rint(2, 11)
               print("Теперь у тебя", player1,"очков")
          elif take_card == "НЕТ":
               inGame1 = False
          else:
               print("Я тебя не понял")

    if inGame2:
          take_card = input("Будешь брать карту?[ДА/НЕТ]")
          if take_card == "ДА":
               player2 += rint(2, 11)
               print(("Теперь у тебя", player2,"очков")
          elif take_card == "НЕТ":
               inGame2 = False
          else:
               print("Я тебя не понял")

    if player1 >= 21:
         inGame1 = False
    if player2 >= 21
         inGame2 = False
 print("Game over")

if player1 <= 21 and player1 > player2:
    print("Player1, you are win!")
elif player2 <= 21 and player2 > player1:
    print("Player2, you are win!")
elif player1 > 21 and player2 > 21:
    print("Никто не выиграл")
else:
          print("Все проиграли")
