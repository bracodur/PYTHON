'''
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество,
номер телефона - данные, которые должны находиться в файле. 1. Программа должна выводить данные 2. Программа
должна сохранять данные в текстовом файле 3. Пользователь может ввести одну из характеристик для
поиска определенной записи(Например имя или фамилию человека) 4. Использование функций. Ваша программа
не должна быть линейной
'''
# 1. создание файла:
#     - открываем файл на дозапись ('a')
# 2. добавление контакта:
#     - запросить у пользователя данные (фио, номер)
#     - открыть файл на дозапись (а)
#     - добавить новый контакт
# 3. вывод данных:
#     - открыть файл на чтение: ('r')
#     - считать файл
#     - вывести на экран
# 4. поиск контакта:
#     - выбор варианта поиска
#     - запросить данные для поиска   0
#     - открываем файл на чтение
#     - считываем данные, сохранить их в переменную
#     - осуществляем поиск контакта
#     - вывод на экран найденный контакта
# 5. создание ui (user interface)
#     -вывести меню на экран
#     -запросить вариант действия
#     -запустить соответствующую функцию
#     -осуществить возможность выхода из программы - зациклили var=? - while...


def input_surname(): #запрашиваем у пользователя новый контакт
    return input ('введите фамилию контакта: ').title()

def input_name():
    return input ('введите имя контакта: ').title()

def input_phone():
    return input ('введите телефон контакта: ').title()

def input_adress():
    return input ('введите адрес контакта: ').title()


def create_contact(): #запрашиваем у пользователя новый контакт
    surname = input_surname()
    name = input_name()
    phone = input_phone()
    adress = input_adress()
    return f"{surname} {name}: {phone}\n{adress}\n\n"


def add_contact(): #функции на действия
    contact_str = create_contact()
    with open ("phonebook.txt", 'a', encoding ='utf-8') as f: # открытие файла в дозапись
        f.write(contact_str)

def print_contacts():
    with open ("phonebook.txt", 'r', encoding ='utf-8') as f: #'r'
        contacs_str = f.read()
    #print ([contacs_str])
    contacs_list = contacs_str.rstrip().split('\n\n')
    for n, contact in enumerate(contacs_list, 1):
        print(n, contact)
    
def serch_contact():
    print(
            'Возможные варианты поиска:\n'
            '1. Фамилия\n'
            '2. Имя\n'
            '3. Телефон\n'
            '4. Адрес'
            )
    
    var = input('выберите вариант поиска: ') #запрашиваем вариант действия

    while var not in ('1', '2', '3', '4'):
            print ('неправильный ввод')
            var = input('выберите вариант поиска: ')
    i_var = int(var)-1
   
    serch = input ('введите критерии поиска: ').title()
    with open ("phonebook.txt", 'r', encoding ='utf-8') as f: #'r'
        contacs_str = f.read()
    contacs_list = contacs_str.rstrip().split('\n\n')

    for str_contacts in contacs_list:
        lst_contact = str_contacts.replace(':','').split()
        if serch in lst_contact[i_var]:
            print(str_contacts)

#========== изменяем контакт ==========
def edit_contact():
    #pass
    print(
            'Возможные варианты Изменения:\n'
            '1. Фамилия\n'
            '2. Имя\n'
            '3. Телефон\n'
            '4. Адрес'
            )
    
    var = input('выберите вариант Изменения: ') #запрашиваем вариант действия

    while var not in ('1', '2', '3', '4'):
            print ('неправильный ввод')
            var = input('выберите вариант Изменения: ')
    i_var = int(var)-1
   
    serch = input ('введите критерии Изменения: ').title()
    with open ("phonebook.txt", 'r', encoding ='utf-8') as f: #'r'
        contacs_str = f.read()
    contacs_list = contacs_str.rstrip().split('\n\n')

    for m, str_contacts in enumerate(contacs_list, 1):
        lst_contact = str_contacts.replace(':','').split()
        if serch in lst_contact[i_var]:
            print(str_contacts)
            var2 = input('Изменить запись? 1-Да, 2-Нет') #запрашиваем вариант действия
            while var2 not in ('1', '2'):
                    print ('неправильный ввод')
                    var2 = input('Изменить запись? 1-Да, 2-Нет')
            i_var2 = int(var2)
            if i_var2 == 1:
                contacs_list[m-1] = create_contact()
                with open ("phonebook.txt", 'w', encoding ='utf-8') as f: # открытие файла в дозапись
                    for n, contact in enumerate(contacs_list, 1):
                        f.write(contact)
                        f.write('\n\n')

#========= удаляем контакт ============
def delete_contact():
    #pass
    print(
            'Возможные варианты удаления:\n'
            '1. Фамилия\n'
            '2. Имя\n'
            '3. Телефон\n'
            '4. Адрес'
            )
    
    var = input('выберите вариант удаления: ') #запрашиваем вариант действия

    while var not in ('1', '2', '3', '4'):
            print ('неправильный ввод')
            var = input('выберите вариант удаления: ')
    i_var = int(var)-1
   
    serch = input ('введите критерии удаления: ').title()
    with open ("phonebook.txt", 'r', encoding ='utf-8') as f: #'r'
        contacs_str = f.read()
    contacs_list = contacs_str.rstrip().split('\n\n')

    for str_contacts in contacs_list:
        lst_contact = str_contacts.replace(':','').split()
        if serch in lst_contact[i_var]:
            print(str_contacts)
            var2 = input('Удалить запись? 1-Да, 2-Нет') #запрашиваем вариант действия
            while var2 not in ('1', '2'):
                    print ('неправильный ввод')
                    var2 = input('Удалить запись? 1-Да, 2-Нет')
            i_var2 = int(var2)
            if i_var2 == 1:
                contacs_list.remove(str_contacts)
                with open ("phonebook.txt", 'w', encoding ='utf-8') as f: # открытие файла в дозапись
                    for n, contact in enumerate(contacs_list, 1):
                        f.write(contact)
                        f.write('\n\n')


#1. создание файла
def interface ():
    with open ("phonebook.txt", 'a', encoding ='utf-8'): # открытие файла в дозапись
        pass #пусто
    
    var = 0
    while var != '6':
        # вывод меню на экран
        print(
            'Возможные варианты:\n'
            '1. Добавить контакт\n'
            '2. Вывести на экран\n'
            '3. Поиск контакта\n'
            '4. Изменить контакт\n'
            '5. Удалить контакт\n'
            '6. Выход'
            )
        print()

        var = input('выберите вариант действия: ') #запрашиваем вариант действия

        while var not in ('1', '2', '3', '4', '5', '6'):
            print ('неправильный ввод')
            var = input('выберите вариант действия: ')
        
        print()

        match var: #if - else
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                serch_contact()
            case '4':
                edit_contact()
            case '5':
                delete_contact()
            case '6':
                print('выход')
        print()


if __name__ == '__main__':
    interface()





#   P Y T H O N  
 