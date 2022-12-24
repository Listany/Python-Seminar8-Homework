# модуль ввода данных от пользователя 

def get_data():
    variant = int(input("Введите 1, если хотите вводить данные через пробел и 2, если хотите вводить данные построчно: "))
    data = ""
    if variant == 1:
        data = input("Введите Фамилию Имя Телефон через пробел: ")
    elif variant == 2:        
        surname = input("Введите фамилию: ")        
        name = input("Введите имя: ")              
        number = input("Введите номер телефона - начиная с 8 - всего 11 цифр: ")
        data = surname + " " + name + " " + number
    return data
        
