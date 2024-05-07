import unittest
from .utils import translate_category, set_amount_int
from .balance import Balance, NoMoney



class TestTranslateCategory(unittest.TestCase):

    def test_translate_income(self):
        self.assertEqual(translate_category('income'), 'Доход')

    def test_translate_expenses(self):
        self.assertEqual(translate_category('expenses'), 'Расход')

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            translate_category('invalid')

class TestSetAmountInt(unittest.TestCase):

    def test_set_amount_int(self):
        # Test with valid integer
        self.assertEqual(set_amount_int('123'), 123)


        # Test with mocking
        set_amount_int('abc')

class TestBalance(unittest.TestCase):

    def test_get_current_balance(self):
        balance = Balance(100)
        self.assertEqual(balance.get_current_balance(), 100)

    def test_add(self):
        balance = Balance(100)
        balance.add(50)
        self.assertEqual(balance.get_current_balance(), 150)

    def test_is_enough(self):
        balance = Balance(100)
        self.assertTrue(balance.is_enough(50))
        self.assertFalse(balance.is_enough(150))

    def test_write_off_enough(self):
        balance = Balance(100)
        balance.write_off(50)
        self.assertEqual(balance.get_current_balance(), 50)

    def test_write_off_not_enough(self):
        balance = Balance(100)
        with self.assertRaises(NoMoney):
            balance.write_off(150)
       
       

if __name__ == '__main__':
    unittest.main()