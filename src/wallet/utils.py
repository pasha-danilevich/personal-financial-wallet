import os

clear = lambda: os.system('cls')

def make_green_text(text: str) -> str:
    return f'\033[32m{text}\033[0m'

def make_red_text(text: str) -> str:
    return f'\033[31m{text}\033[0m'

def translate_category(category):
    result = ''
    if category == 'income':
        result = 'Доход'
    elif category == 'expenses':
        result = 'Расход'
    else:
        raise ValueError(f'Invalid category {category}')
    return result

def set_amount_int(value):
    try:
        value = int(value)
        return value
    except ValueError:
        clear()
        print(make_red_text("Для изменения суммы введите число!"))
  
    

INTERFACE = """
Что надо сделать:    
    Показать баланс - 1  
    Показать доходы - 2  
    Показать расходы - 3 
    Добавить транзакцию - 4 
    Поиск - 5 
    Редактировать запись - 6
    Завершить работу - 0 
      
Выберете действие: """

ADD_TRANSACTION_INTERFACE = """
Через пробел, не нарушая порядок, введите:
    1. Категорию ('income' или 'expenses') 
    2. Сумму
    3. Описание 

Отменить создание - 0
Введите категорию ('income' или 'expenses'): """

SERCH_INTERFACE = """
Выберите поле, по которому будет проходить поиск:
    По категории - 1
    По сумме - 2
    По описанию - 3 
  
Отменить поиск - 0
Выберите поле: """

UPDATE_SERCH_INTERFACE = """
Чтобы обновить запись, вы должны выбрать ее.
Выберите поле, по которому будет проходить поиск:
    По категории - 1
    По сумме - 2
    По описанию - 3 
  
Отменить поиск - 0
Выберите поле: """

UPDATE_INTERFACE = """
Выберите поле, которое хотите изменить:
    1. Категорию ('income' или 'expenses') 
    2. Сумму
    3. Описание 
  
Отменить выбор - 0
Выберите поле: """
