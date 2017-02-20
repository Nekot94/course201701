king = {
    'Стивен Кинг':
        ['Оно','Сияние','Кэрри','Противостояние','Мизери']}
rowling = {
    'Дж.К.Роулинг':['Гарри Поттер и Философский камень','Гарри Поттер и Тайная комната','Гарри Поттер и Узник Азкабана','Гарри Поттер и Кубок огня',
    'Гарри Поттер и Орден Феникса','Гарри Поттер и Принц-полукровка','Гарри Поттер и Дары Смерти']}
other = {}
print('Данные для входа в тестовый аккаунт\n'
'Логин:test\n'
'Пароль:тест\n')

def main():
    log = input('У вас есть аккаунт?:'.lower())
    if log == 'да':
        login = input('Введите логин:')
        password = input('Введите пароль:')
        bd_login = open('bd_login.txt','r')
        bd_password = open('bd_password.txt','r')
        bd_login_read = bd_login.read()
        bd_password_read = bd_password.read()
        if login in bd_login_read or login == 'test' and password in bd_password_read or password == 'test' :
            print('Вы авторизовались.Доступный список:')
            while True:
                list = ['1.Добавить автора и книгу','2.Посмотреть доступных авторов']
                for i in list:
                    print(i)
                choice = input('Ваш выбор: ')
                if choice == '1':
                    name = input('Введите имя автора:')
                    book = input('Введите название книги:')
                    bd_books = open('bd_books.txt','a')
                    bd_authors = open('bd_authors.txt','a')
                    bd_authors.write(name)
                    bd_books.write(book)
                    bd_books.close()
                    bd_authors.close()
                if choice == '2':
                    bd_authors = open('bd_authors.txt','r')
                    bd_books = open('bd_books.txt','r')
                    bd_authors_read = bd_authors.readline()
                    print(bd_authors_read)
                    bd_books_read = bd_books.readline()
                    print(bd_books_read)

                else:
                    print('Такого пункта нет')

    else:
        logg = input('Хотите зарегистрироваться?:')
        if logg == 'да':
            log_reg = input('Введите имя пользователя:')
            pas_reg = input('Введите пароль:')
            bd_login = open('bd_login.txt','a')
            bd_password = open('bd_password.txt','a')
            bd_login.write(log_reg + '\n')
            bd_password.write(pas_reg + '\n')
            bd_login.close()
            bd_password.close()
            print('Вы успешно зарегестрировались!\
                Можете пользоваться программой.')
        else:
            print('Ваши права будут ограничены.\n'
            'Вы не сможете добавлять книги и авторов')
        while True:
            list = ['1.Добавить автора и книгу', '2.Посмотреть доступных авторов']
            for i in list:
                print(i)
            choice_unlog = input('Ваш выбор:')
            if choice_unlog == '1':
                print('Недоступно для неавторизованных пользователей, используйте тестовый аккаунт.')
            if choice_unlog == '2':
                print('Книги Стивена Кинга:')
                for i in king['Стивен Кинг']:
                    print(i)
                print('\n\n\nКниги Дж.К.Роулинг:')
                for i in rowling['Дж.К.Роулинг']:
                    print(i)
            if choice_unlog != '1' and choice_unlog != '2':
                print('Такого пункта нет.')

main()