import table_link

def  write_file_name ( entry ):   # Запись в файл
    with open('name.csv', 'a') as file:
        file.write(f'{entry[0]};{entry[1]};{entry[2]};{entry[3]};\
            {entry[4]};{entry[5]};{entry[6]};{entry[7]};\n')

def  write_file_class ( entry ):   # Запись в файл
    with open('clas.csv', 'a') as file:
        file.write(f'{entry[0]};{entry[1]};{entry[2]};{entry[3]};\n')

def  write_file_adress ( entry ):   # Запись в файл
    with open('adress.csv', 'a') as file:
        file.write(f'{entry[0]};{entry[1]};{entry[2]};{entry[3]};\
            {entry[4]};{entry[5]};\n')


