# Главный модуль
import controller

while True:
    var = int(input('Введите 1, чтобы ввести данные и 2 чтобы найти данные: '))
    
    if var == 1:
        controller.button_input()        
    elif var == 2:
        controller.button_output()
    else:
        print("Вы ввели неверные данные")
        
    exit = int(input("Хотите продолжить - введите 1, хотите завершить - нажмите любую другую клавишу: "))
    if exit != 1:
        break
