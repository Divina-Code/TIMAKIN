import random

letters = list('abcdefg')
symb = list('!@#$%^&*()_')
pas = ' '
for a in range(8):
    pas = pas + random.choice(letters)
print("Ваш пароль из букв", pas )
symb = list("1234567890!@%^&*()_+abcdefg")
ps = ' '
for a in range(8):
    ps = ps + random.choice(symb)
print("Пароль из различныз символов: ", ps)

