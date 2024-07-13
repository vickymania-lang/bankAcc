from bank_account import *

Vic = BankAccount(1000, "Vic")
Ola = BankAccount(2000, "Ola")

Vic.getBalance()
Ola.getBalance()

Ola.deposit(500)

Vic.withdraw(10000)
Vic.withdraw(10)

Vic.transfer(10000, Ola)
Vic.transfer(100, Ola)

Mania = InterestRewardsAcct(1000, 'Mania')

Mania.getBalance()

Mania.deposit(10000)

Mania.transfer(10, Vic)

Bola = SavingAcct(1000, 'Mania')

Bola.getBalance()

Bola.deposit(100)

Bola.transfer(1000, Mania)
Bola.transfer(500, Mania)
