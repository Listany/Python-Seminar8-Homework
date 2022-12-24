# модуль добавления запрошенных данных в базу данных - в 2 типа файла - txt, csv
import input


def add_db():
    user_info = input.get_data()
    with open ('db.txt', 'a') as f:
        f.write(f'{user_info} \n')
    with open ('db.csv', 'a')  as f1:
        f1.write(f'{user_info} \n') 
