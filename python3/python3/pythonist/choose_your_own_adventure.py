name = input("Введите свое имя: ")
print("Добро пожаловать", name, "к этому приключению!")

answer = input(
    "Вы находитесь на грунтовой дороге, она заканчивается, и вы можете пойти налево или направо. По какой дороге вы хотите пойти?").lower()

if answer == "налево":
    answer = input("")
elif answer == "вправо":
    print()    
else:
    print("Не является допустимым вариантом. Вы теряете")