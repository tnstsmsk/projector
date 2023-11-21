import unittest
from unittest.mock import patch
from bank_model import Bank, SavingsAccount, CurrentAccount


class TestBank(unittest.TestCase):

    def test_open_account(self):
        bank = Bank()
        account = SavingsAccount(1, 1000, 3.0)
        bank.open_account(account)
        self.assertIn(account, bank.accounts)
        self.assertEqual(account.balance, 1000)

    @patch('builtins.print')
    def test_update_accounts(self, mock_print):
        bank = Bank()
        savings = SavingsAccount(1, 1000, 3.0)
        current = CurrentAccount(2, -100, -200)
        bank.open_account(savings)
        bank.open_account(current)
        bank.update_accounts()

        self.assertEqual(savings.balance, 1030.0)  # 1000 + 3% of 1000

        mock_print.assert_called_with(f"Overdraft letter sent for Account 2")


if __name__ == '__main__':
    unittest.main()
