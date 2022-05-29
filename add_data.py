import uuid
from datetime import datetime

def add_anketa():
   
    list_name = []
    list_name.append(uuid.uuid4())
    list_name.append(input('Фамилия: ').title())
    list_name.append(input('Имя: ').title())
    list_name.append(input('Отчество: ').title())
    list_name.append(datetime.strptime(input('Дата рождения (ддммгггг): '),'%d%m%Y'))
    list_name.append(input('Класс: '))
    list_name.append(input('Статус: ').title())

    list_class = []
    list_class.append(uuid.uuid4())
    list_class.append(int(input('Ряд в классе: ')))
    list_class.append(int(input('Номер парты: ')))
    list_class.append(int(input('Вариант: ')))

    list_name.append(list_class[0])
    
    list_adress = []
    list_adress.append(list_name[0])
    list_adress.append(input('Город: ').title())
    list_adress.append(input('Улица: ').title())
    list_adress.append(input('Дом: '))
    list_adress.append(input('Квартира: '))
    list_adress.append(input('Примечание: ').title())

    print('\nВами введена запись: ',list_name[1:7],'\n', list_class[1:],'\n', list_adress[1:])
    return list_name, list_class, list_adress

