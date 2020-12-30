import random
word = ['Орёл , сова , зяблик , январь , февраль , декабрь , мороз , снег , лед ']
letters = word[random.randrange(3)]
Spisok_letters = len(letters)
Gizni = 5
game = False
ispol_letters = ""
vse_slovo = []
for a in range(len(word)):
    vse_slovo += '_'
while Spisok_letters != 0 and Gizni:
    game = False
    while True:
        letter =input('Напиши букву')
        if len(letter) > 1:
            print("Надо писать одну букву")
        else:
            ispol_letters += letter
            break
    schet = 0
        for a in letters:
            if letter in a :
                Spisok_letters -= 1
            game = True
            vse_slovo[schet] = letter
        schet += 1
    if not test :
        Gizni -=1
        print('Неа - 1 hp')
    else:
        print('Ага , молодец')
        print(vse_slovo)
    print("У тебя ", Gizni)
if (Spisok_letters == 0)
    print("Ну ты крутой . Ты угадал. Это было" , word)
else:
    print('Сорян , проиграл . Давай еще!')
