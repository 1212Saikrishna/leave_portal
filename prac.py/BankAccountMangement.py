# To Raise Exception For ViableTransaction create class
class BalanceException(Exception):
    pass

# To Open An BankAccount:
class BankAccount:
    def __init__(self,intialAmount,acctName):
        self.balance = intialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance is ${self.balance:.2f}")
# b1=BankAccount(25555.23,'Saikrishna')
# print(b1)
    # creating method to getBalance
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance is ${self.balance:.2f}")

    # creating method to deposit
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete")
        self.getBalance()
    # creating method to viableTransaction
    def viableTransaction(self,amount):
        if self.balance < amount:
            raise BalanceException(f"\nSorry,'{self.name}' your balance is {self.balance:.2f}")
    # creating method to withdraw
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as e:
            print(f"\nWithdraw Interrupted: {e}")
    # creating method to transfer
    def transfer(self,amount,account):
        try:
            print('\n**********\n\nTransfer Beginning..')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed!\n\n**********')
        except BalanceException as e:
            print(f"\Transfer Interrupted: {e}")

# To reward interest for every deposit
class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        # Call the parent class's deposit method first
        super().deposit(amount)
        # Apply interest
        self.balance = self.balance + (amount * 0.05)
        print('\nDeposit Complete')
        self.getBalance()

# Savings Account with fees
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        # Call the parent class's constructor
        super().__init__(initialAmount, acctName)
        self.fee = 5
    def withdraw(self, amount):
        try:
            total_amount = amount + self.fee
            self.viableTransaction(total_amount)
            self.balance = self.balance - (total_amount)
            print('\nWithdraw Completed.')
        except BalanceException as e:
            print(f"Withdraw Interrupted: {e}")