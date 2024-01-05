# correct solution
class User:
    def __init__(self, name, last_name, age, profession = None):
        self.__name = name 
        self.__last_name = last_name
        self.__age = age

        if profession:
            self.__profession = profession
        else:
            self.__profession = 'absent'
    
    @property
    def get_user(self):
        return f"Name : {self.__name} \nLast_name : {self.__last_name} \nAge : {self.__age} \nprofession : {self.__profession}"
    
    @get_user.setter
    def get_user(self, *args ):
        for name, value in zip(self.__dict__.keys(), *args):
            if value:
                self.__dict__[name] = value


user = User('a', 'b', 20)
user.get_user = ("nikita", 'marykov', 20, 'programmer')


class SaveDataDb:
    def saveUser(self, data_user):
        with open(r'db.txt', 'a') as file:
            file.write(f'\n\n{data_user}')


data = SaveDataDb().saveUser(user.get_user)



# wrong decision
class User:
    def __init__(self, name, last_name, age, profession = None):
        self.__name = name 
        self.__last_name = last_name
        self.__age = age

        if profession:
            self.__profession = profession
        else:
            self.__profession = 'absent'
    
    @property
    def get_user(self):
        return f"Name : {self.__name} \nLast_name : {self.__last_name} \nAge : {self.__age} \nprofession : {self.__profession}"
    
    @get_user.setter
    def get_user(self, *args ):
        for name, value in zip(self.__dict__.keys(), *args):
            if value:
                self.__dict__[name] = value

    def saveUser(self, data_user):
        with open(r'db.txt', 'a') as file:
            file.write(f'\n\n{data_user}')

user = User('a', 'b', 20)
user.get_user = ("nikita", 'marykov', 20, 'programmer')
data = User.saveUser(user.get_user)