import json


class Account:

    last_id = None
    ACC_FILE = "AirgeadCryptoAccount.json"


    def __init__(self, id, name, balance):
        self.id = id
        self.name = name
        self.balance = balance

    def increase_balance(self, amount):
        self.balance += amount

    def decrease_balance(self, amount):
        self.balance -= amount

    def add_account(self, name, start_balance):
        account_dic = {"Account ID": self.last_id+1, "Name":name, "Balance": start_balance, "Transactions": []}
        account_json = json.dumps(account_dic)
        return account_dic

    def save_account(self, acc_json):
        return

    def amend_balance(self, amount):
        return

    def first_accounts(self):
        if self.last_id is None:
            self.last_id = 0
            self.add_account("System", 0)
            self.add_account("Alice", 100)
            self.add_account("Bob", 100)

    def add_transaction(self, from_acc, to_acc, amount):

        return

