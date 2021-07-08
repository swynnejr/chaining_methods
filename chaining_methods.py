class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
    	self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
        print(self.name)

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
travis = User("Travis Douglass", "TDugzzz@HaloReach.com")
maddox = User("Maddox Womble", "MadFox420@WSMFP.com")

# My chain below doesnt work.... VVVVVVV

# guido.make_deposit(100).make_deposit(200).make_withdrawl(75).display_user_balance()

guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()



print(guido.account_balance) # this works
