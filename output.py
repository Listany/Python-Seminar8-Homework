# модуль вывода данных по запросу
def get_info():
    info = input("Введите информацию для поиска: ")    
    with open ('db.csv', 'r')  as f1:        
        while True:
            line = f1.readline()    
            if not line:
                break
            if info in line:    
                print(line.strip())
    
    
