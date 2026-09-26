from abc import ABC, abstractmethod
class Users(ABC):
    users_count=0
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        Users.users_count+=1
        
    def check_password(self, entered_password):
        if entered_password == self.__password:
            return True
        else:
            return False
        
    @abstractmethod
    def access_level(self):
        pass
class Adminuser(Users):
    def access_level(self):
        return "Full access: read, write, delete"
class Regularuser(Users):
    def access_level(self):
        return "Limited access: read only"

a1 = Adminuser("admin1", "pass123")
r1 = Regularuser("user1", "pass456")

print(a1.check_password("wrongpass"))    # False
print(a1.check_password("pass123"))       # True
print(a1.access_level())
print(r1.access_level())
print(Users.users_count)
    

