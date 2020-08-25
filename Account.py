

class Account:

    def __init__(self, name, acc_id):
        self.name = name
        self.acc_id = acc_id
        self.balance = 0

    def increase_balance(self, amount):
        self.balance += amount

    def decrease_balance(self, amount):
        self.balance -= amount

    def account_dict(self):
        acc_dict = {'Account ID': self.acc_id, 'Name': self.name, 'Balance': self.balance}
        return acc_dict
