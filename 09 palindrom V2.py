print("Привет!")
palindrom = input("Напиши палиндром ").lower()
palindrom = palindrom.split(' ')
print(palindrom)
for Pl1 in palindrom:
    palEdrom = Pl1[::-1].lower()
    if Pl1.lower() == palEdrom:
        print(Pl1, 'да ,они палиндром')
    else:
        print(Pl1, " нет, не палиндром")
print("Спасибо, что заглянули")

