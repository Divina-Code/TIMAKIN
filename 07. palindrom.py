print("Привет!")
palindrom = input("Напиши палиндром ").lower()
palEdrom = (palindrom[::-1])
 if palindrom == palEdrom :
     print("Ага, это палиндром")
 else:
     print("Неа , это не палиндром")
