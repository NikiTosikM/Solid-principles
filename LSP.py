class Bank:
    def __init__(self, name_user, last_name, count_money):
        self.__name_user = name_user
        self.__last_name = last_name
        self.__count_money = count_money

    def getUserAccount(self, *args):
        changedData = {}
        for name, value in zip(Bank.__dict__, *args):
            if value:
                Bank.__dict__[name] = value
                changedData[name] = value
        
        for name, value in changedData.items():
            print(f'{name} {value}', end='\n')


# wrong decision ( You cannot override methods of a parent class )
class User(Bank):
    def getUserAccount(self, name_user= None, last_name= None, count_money= None):
        self.__name_user = name_user
        self.__last_name = last_name
        self.__count_money = count_money
        
        