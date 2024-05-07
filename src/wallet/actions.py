from utils import * 
from transactions import Transaction
from balance import NoMoney
from file_manager import FinanceManager
from main import main
manager = FinanceManager()



def view_balance():
    """
    Выводит текущий баланс.
    """
    balance = make_green_text(manager.get_balance())
    print(f'Ваш баланс: {balance}')


def view_list(transaction_list, is_update):
    """
    Выводит список транзакций.
    
    Args:
        transaction_list (list): Список транзакций.
        is_update (bool): Флаг обновления.
    """
    number = 0
    if len(transaction_list) == 1 and is_update:
        get_transaction(transaction_list)
    for transaction in transaction_list:
        number += 1
        transaction_obj = Transaction.deserialize(transaction)
        print(f"Запись номер: {number}", transaction_obj.view())
    print(f'Всего: {number}')


def get_transaction(transaction_list):
    """
    Выбирает транзакцию для обновления.
    
    Args:
        transaction_list (list): Список транзакций.
    
    Returns:
        Transaction: Выбранная транзакция.
    """
    if len(transaction_list) > 1:
        transaction_number = int(input("Выбрать запись под номером: ")) - 1
    else:
        transaction_number = 0
    transaction_obj = Transaction.deserialize(transaction_list[transaction_number])
    clear()
    print('Выбрана следующая запись:', make_green_text(transaction_obj.view()))
    return transaction_obj


def add_transaction():
    """
    Добавляет новую транзакцию.
    """
    category = input(ADD_TRANSACTION_INTERFACE)
    if category == '0' or '':
        return clear()
    amount = input('Введите сумму: ')
    description = input('Введите описание: ')
    try:
        transaction = Transaction(
            category=category,
            amount=amount,
            description=description
            )
        manager.add_transaction(transaction)
        clear()
        print(make_green_text(f'Вы создали: \n{transaction.view()}'))
    except ValueError:
        clear()
        print(make_red_text("Неверно введенная категория. Введите 'income' или 'expenses'"))
    except NoMoney:
        clear()
        print(make_red_text("Недостаточно средств для расходов"))


def search_on_field(field, value, is_update):
    """
    Ищет транзакции по заданному полю и значению.
    
    Args:
        field (str): Поля для поиска.
        value (str): Значение для поиска.
        is_update (bool): Флаг обновления.
    
    Returns:
        list: Список найденных транзакций.
    """
    if field == 'category' and value == None:
        value = input("Введите зачение для поиска по категории ('income' или 'expenses'): ")
    elif field == 'category' and value:
        pass
    else:
        value = input('Введите зачение для поиска: ')
    transaction_list = manager.search_transactions_on_field(field, value)
    clear()
    if len(transaction_list) == 0:
        print("По такому запросу ничего не найдено") 
    else:
        view_list(transaction_list, is_update)
        
        if is_update:
            transaction_obj = get_transaction(transaction_list)
            
            field = input(UPDATE_INTERFACE)
            value = input('Введите зачение для обновления: ')
            select_update_field(field, value, transaction_obj)
    
            
def update_on_field(field, value, transaction_obj):
    """
    Обновляет транзакцию.
    
    Args:
        field (str): Поля для обновления.
        value (str): Значение для обновления.
        transaction_obj (Transaction): Транзакция для обновления.
    
    Returns:
        Transaction: Обновленная транзакция.
    """
    updated_obj = manager.update_transaction(
        field=field,                       
        value=value, 
        transaction_obj=transaction_obj
    )
    clear()
    print(make_green_text('Обновленная запись: '), updated_obj.view())
    
    
def select_search_action(is_update=False):
    """
    Выбирает действие для поиска.
    
    Args:
        is_update (bool): Флаг обновления.
    
    Returns:
        str: Результат выбора.
    """
    if is_update:
        request = input(UPDATE_SERCH_INTERFACE)
    else:
        request = input(SERCH_INTERFACE)
    process_search_request(request, is_update)


def process_search_request(request: str, is_update: bool) -> str:
    """
    Обрабатывает результат выбора.
    
    Args:
        request (str): Результат выбора.
        is_update (bool): Флаг обновления.
    
    Returns:
        str: Результат обработки.
    """
    if request == '1':
        return search_on_field('category', None, is_update)
    elif request == '2':
        return search_on_field('amount', None, is_update)
    elif request == '3':
        return search_on_field('description', None, is_update)
    elif request == '0':
        clear()
    else:
        clear()
    return ''


def select_update_field(request: str, value: str, transaction_obj: Transaction) -> str:
    """
    Выбирает поле для обновления.
    
    Args:
        request (str): Результат выбора.
        value (str): Значение для обновления.
        transaction_obj (Transaction): Транзакция для обновления.
    
    Returns:
        str: Результат выбора.
    """
    if request == '1':
        return update_on_field('category', value, transaction_obj)
    elif request == '2':
        return update_on_field('amount', value, transaction_obj)
    elif request == '3':
        return update_on_field('description', value, transaction_obj)
    elif request == '0':
        clear()
    else:
        clear()
    return ''


def update_transaction():
    """
    Обновляет транзакцию.
    """
    select_search_action(is_update=True)
