password = input("Введите пароль: ")
password_repeat = input("Подтвердите пароль: ")
if password == password_repeat:
    print("Пароль совпадает")
else:
    print("Ошибка, попробуйте еще раз")