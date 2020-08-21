import json


class Account:

    last_id = None
    ACC_FILE = "AirgeadCryptoAccount.json"
    balance = 0
    transactions = []


    def __init__(self, name, id):
        self.name = name
        self.id = id


    def increase_balance(self, amount):
        self.balance += amount

    def decrease_balance(self, amount):
        self.balance -= amount

    def add_account(self, name, start_balance):
        account_dic = {"Account ID": self.last_id+1, "Name":name, "Balance": self.balance, "Transactions": []}
        account_json = json.dumps(account_dic)
        return account_dic

    def save_account(self, acc_json):

        return

    def amend_balance(self, amount):
        return


    def add_transaction(self, from_acc, to_acc, amount, note):
        trans_dic = {"From Account": from_acc, "To Account": to_acc, "Amount": amount, "Note": note}
        trans_json = json.dumps(trans_dic)

        return trans_json

    def set_balance(self):
        return



