from BankAccountMangement import *

# Creating Instance of BankAccount

# Morin = BankAccount(7500,"Morin Depp")
Lappe = BankAccount(8500,"Lappe Run")

# # calling getbalance method
# Morin.getBalance()
# Lappe.getBalance()

# # calling deposit method
# Morin.deposit(6000)
# Lappe.deposit(1000)

# # calling withdraw method
# Morin.withdraw(500)


# Morin.transfer(1500,Lappe)
# Morin.getBalance()

# Jim = InterestRewardsAcct(10000,"Jimme Crap")
# Jim.getBalance()
# Jim.deposit(500)
# Jim.transfer(5000,Lappe)
Ramt = SavingsAcct(10000,"Ramt Sas")
Ramt.getBalance()
Ramt.deposit(500)
Ramt.transfer(5000,Lappe)
Ramt.withdraw(500)
Ramt.getBalance()