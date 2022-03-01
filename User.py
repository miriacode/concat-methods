class User:
    def __init__(self,name):
        self.name = name
        self.dollars = 0

    def make_a_deposit(self,amount):
        self.dollars += amount
        return self
    
    def withdraw_money(self,amount):
        self.dollars -= amount
        return self

    def show_balance(self):
        print(f'User: {self.name}, Balance: ${self.dollars}')
    
    #Bonus
    def transfer_money(self,other_user,ammount):
        self.dollars -= ammount
        other_user.dollars += ammount
        return self

    
