import datetime
import uuid

from utils import translate_category

class Transaction():
    def __init__(self, category, amount, description, data=None, id=None):
        
        if category not in ['income', 'expenses']:
            raise ValueError('Invalid category')
        
        if data: self.date = data
        else: self.date = str(datetime.date.today())
            
        if id: self.id = id
        else: self.id = uuid.uuid1()  
          
        self.category = category
        self.amount = abs(int(amount))
        self.description = description
        
    @staticmethod
    def deserialize(json_obj: dict) -> 'Transaction':
        """
        Создает объект Transaction из словаря с данными.
        
        Args:
            json_obj (dict): Словарь с данными транзакции.
        
        Returns:
            Transaction: Объект Transaction, созданный из данных словаря.
        """
        transaction = Transaction(
            id=json_obj['id'],
            data=json_obj['data'],
            category=json_obj['category'],
            amount=json_obj['amount'],
            description=json_obj['description']
        )
        return transaction

    def serialize(self) -> dict:
        """
        Преобразует объект Transaction в словарь с данными.
        
        Returns:
            dict: Словарь с данными транзакции.
        """
        return {
            'id': int(self.id),
            'data': self.date,
            'category': self.category,
            'amount': self.amount,
            'description': self.description
        }

    def view(self) -> str:
        """
        Возвращает строковое представление транзакции.
        
        Returns:
            str: Строковое представление транзакции.
        """
        category = translate_category(self.category)
        
        return f"""
    Дата: {self.date}
    Категория: {category}
    Сумма: {self.amount}
    Описание: {self.description}
    ---"""
