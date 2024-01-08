from abc import ABC, abstractmethod


class SuperUser(ABC):
    @abstractmethod
    def GetUsers(self):
        pass

    @abstractmethod
    def EditPassword(self):
        pass


class CreateSuperUser(SuperUser):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def GetUsers(self):
        with open(r'db.txt', 'r') as file:
            for line in file:
                print(line)

    def EditPassword(self, password):
        self.password = password


# correct solution
class User(ABC):
    @abstractmethod
    def EditPassword(self):
        pass        

class CreateUser(User):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def EditPassword(self, password):
        self.password = password

    
# wrong decision
class CreateUser(SuperUser):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def GetUsers(self):
        pass

    def EditPassword(self, password):
        self.password =  password
        
