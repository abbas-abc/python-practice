class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public
        self.__balance=balance  #private
    def get_balance(self):
        return self.__balance 
    
    def set_balance(self,newBalance):
        self.__balance=newBalance
        
    
a1= BankAccount("Afaq",1000)
a1.set_balance(20_000)
print(a1.name, a1.get_balance())

