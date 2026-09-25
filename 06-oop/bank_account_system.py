from abc import ABC, abstractmethod
class BankAccount(ABC):
    total_accounts=0
    
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
        BankAccount.total_accounts+=1

    def get_balance(self):
        return self.__balance

    @classmethod
    def get_total_accounts(cls):
        return cls.total_accounts

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingAccount(BankAccount):
    def calculate_interest(self):
        return self.get_balance()*0.5
class CurrentAccount(BankAccount):
    def calculate_interest(self):
        return self.get_balance()*0

    
S1=SavingAccount("Ali",1000)
C1=CurrentAccount("Khan",2000)

print(f"Saving Account balance: {S1.get_balance()},Interest: {S1.calculate_interest()}")
print(f"Current Account balance: {C1.get_balance()},Interest: {C1.calculate_interest()}")
print(f"Number of accounts: {BankAccount.get_total_accounts()}")

    
