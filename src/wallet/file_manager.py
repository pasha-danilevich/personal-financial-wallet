from transactions import Transaction
from balance import Balance
import json
import os

from utils import set_amount_int

import os
import json

class FileManager:
    def __init__(self, filename='src/data.json'):
        """
        Инициализирует объект FileManager с указанным именем файла.
        
        Args:
            filename (str): Имя файла для загрузки и сохранения данных.
        """
        self.filename = filename

    def load_data(self) -> dict:
        """
        Загружает данные из файла JSON.
        
        Returns:
            dict: Загруженные данные или пустой словарь, если файл не существует.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return {'balance': 0, 'transactions': []}

    def save_data(self, data: dict) -> None:
        """
        Сохраняет данные в файл JSON.
        
        Args:
            data (dict): Данные для сохранения.
        """
        with open(self.filename, 'w') as file:
            json.dump(data, file)


class FinanceManager:
    def __init__(self):
        self.file_manager = FileManager()
        self.data = self.file_manager.load_data()
    

    def get_balance(self):
        balance = Balance(self.data['balance'])
        return balance.get_current_balance()
    

    def add_transaction(self, transaction: Transaction):
        wallet = Balance(self.data['balance'])

        # Обрабатываем транзакцию в зависимости от ее категории
        if transaction.category == 'expenses':
            wallet.write_off(transaction.amount)
        elif transaction.category == 'income':
            wallet.add(transaction.amount)

        # Обновляем баланс в данных
        self.data['balance'] = wallet.get_current_balance()

        # Добавляем транзакцию в список транзакций
        self.data['transactions'].append(transaction.serialize())

        # Сохраняем обновленные данные
        self.file_manager.save_data(self.data)



    def update_transaction(self, transaction_obj: Transaction, field: str, value: str) -> Transaction:
        transactions = self.data['transactions']
        updated_transaction = None

        # Преобразуем значение поля 'amount' в целое число
        if field == 'amount':
            value = set_amount_int(value)

        # Находим и обновляем транзакцию
        for transaction in transactions:
            if transaction['id'] == transaction_obj.id:
                if value:
                    transaction[field] = value
                    updated_transaction = transaction
                    break
                else:
                    break

        # Сохраняем обновленные данные
        self.file_manager.save_data(self.data)

        # Возвращаем обновленный объект транзакции
        return Transaction.deserialize(updated_transaction)
    
    def search_transactions_on_field(self, field: str, value: str) -> list[dict]:
        transactions = self.data['transactions']
        matching_transactions = []

        # Преобразуем значение поля 'amount' в целое число
        if field == 'amount':
            value = set_amount_int(value)

        # Находим транзакции, соответствующие заданному полю и значению
        for transaction in transactions:
            if transaction[field] == value:
                matching_transactions.append(transaction)

        return matching_transactions

