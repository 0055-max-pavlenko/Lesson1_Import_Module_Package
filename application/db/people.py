def get_employees(file_name):
    with open(file_name, 'r', encoding = 'utf-8') as file:
        print('Список сотруднков:')
        for i in file.readlines():
            print(f'{i}', end = '')

