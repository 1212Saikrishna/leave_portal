import unittest
from BankAccountMangement import *

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        acct = BankAccount(100, 'TestAccount')
        acct.deposit(50)
        self.assertEqual(acct.balance, 150)

    def test_withdraw(self):
        acct = BankAccount(100, 'TestAccount')
        acct.withdraw(50)
        self.assertEqual(acct.balance, 50)

    def test_interest_rewards(self):
        acct = InterestRewardsAcct(100, 'TestAccount')
        acct.deposit(50)
        self.assertEqual(acct.balance, 152.5)  # 150 + 50 * 0.05 = 157.5

class TestSavingsAcct(unittest.TestCase):
    def test_savings_withdraw(self):
        acct = SavingsAcct(100, 'TestAccount')
        acct.withdraw(10)
        self.assertEqual(acct.balance, 85)  # 100 - 10 - 5 (fee)

    def test_savings_withdraw_insufficient_funds(self):
    # Create a SavingsAcct with an initial balance
        acct = SavingsAcct(100.0, "TestAccount")
    
    # Attempt to withdraw an amount greater than the balance
        with self.assertRaises(BalanceException):
            acct.withdraw(110.0)  # This should raise a BalanceException
    
    # You can add additional assertions if needed
        self.assertEqual(acct.balance, 100.0)  # Balance should not change after a failed withdrawal


if __name__ == '__main__':
    unittest.main()
