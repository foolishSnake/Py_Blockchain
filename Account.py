class Account:

    id = None
    name = None
    balance = 0

    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def increse_balance(self, amount):
        self.balance += amount

    def decrese_balance(self, amount):
        self.balance -= amount
