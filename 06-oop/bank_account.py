class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public
        self.__balance=balance  #private
    def get_balance(self):
        return self.__balance 
    
a1= BankAccount("Afaq",1000)
print(a1.name, a1.get_balance())

