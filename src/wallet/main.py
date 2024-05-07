from actions import *
from utils import clear, INTERFACE


is_end = False

"""Вместо использования оператора match я использовал серию if-elif-else
проверок. Это связано с тем, что оператор match был введен в Python 3.10, 
а я хочу сделать код совместимым с Python 3.6+.
"""
def select_action(value: str) -> str:
    """
    Выбирает и выполняет соответствующее действие на основе введенного значения.
    
    Args:
        value (str): Значение, введенное пользователем.
    
    Returns:
        str: Результат выполнения выбранного действия.
    """
    clear()  # очищает консоль

    if value == '1':
        return view_balance()
    elif value == '2':
        return search_on_field('category', 'income', is_update=False)
    elif value == '3':
        return search_on_field('category', 'expenses', is_update=False)
    elif value == '4':
        return add_transaction()
    elif value == '5':
        return select_search_action()
    elif value == '6':
        return update_transaction()
    elif value == '0':
        return end()
    else:
        return main()

def end() -> str:
    """
    Завершает работу программы.
    
    Returns:
        str: Сообщение о завершении работы.
    """
    global is_end
    print('Конец работы')
    is_end = True
    return ''

def main() -> None:
    """
    Основной цикл программы, который запрашивает и обрабатывает действия пользователя.
    """
    clear()
    
    while True:
        request = input(INTERFACE)
        response = select_action(request)
        
        if is_end:
            break

            

if __name__ == "__main__": 
    main()