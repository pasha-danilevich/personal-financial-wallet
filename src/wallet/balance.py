class NoMoney(Exception):
    """
    Исключение, возникающее при попытке списания средств, когда их недостаточно на балансе.
    """
    pass

class Balance:
    def __init__(self, balance: int):
        """
        Инициализирует объект Balance с указанным начальным балансом.
        
        Args:
            balance (int): Начальный баланс.
        """
        self._balance = balance
    
    def get_current_balance(self) -> int:
        """
        Возвращает текущий баланс.
        
        Returns:
            int: Текущий баланс.
        """
        return int(self._balance)
    
    def add(self, amount: int) -> None:
        """
        Увеличивает баланс на указанную сумму.
        
        Args:
            amount (int): Сумма для добавления.
        """
        self._balance += amount
    
    def is_enough(self, amount: int) -> bool:
        """
        Проверяет, достаточно ли средств на балансе для списания указанной суммы.
        
        Args:
            amount (int): Сумма для проверки.
        
        Returns:
            bool: True, если средств достаточно, иначе False.
        """
        return self._balance >= amount
        
    def write_off(self, amount: int) -> None:
        """
        Списывает указанную сумму со счета.
        
        Args:
            amount (int): Сумма для списания.
        
        Raises:
            NoMoney: Если средств недостаточно для списания.
        """
        if self.is_enough(amount):
            self._balance -= amount
        else:
            raise NoMoney("Недостаточно средств на балансе")

    
    