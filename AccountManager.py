from Account import Account
import os.path
import csv


class AccountManager:
    accounts = []
    last_id = 0
    CSV_HEADER = ['Account ID', 'Name', 'Balance']
    ERROR_CODES = {1: "Record Not Found", 2: "File Not Found", 3: "Success"}

    def __init__(self, account_file):
        self.account_file = account_file
        self.get_last_id()

    def add_account(self, name):
        new_acc = Account(self.last_id + 1, name)
        self.accounts.append(new_acc)
        self.last_id += 1
        self.write_account(new_acc)

        return

    def get_last_id(self):
        if os.path.isfile(self.account_file):
            with open(self.account_file, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    self.last_id = int(line['Account ID'])
                return 3

        else:
            return 2

    def get_account_file(self, acc_num):
        if os.path.isfile(self.account_file):
            with open(self.account_file, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    if int(line['Account ID']) == acc_num:
                        new_acc = Account(int(line['Account ID']), line['Name'])
                        new_acc.balance = int(line['Balance'])
                        self.accounts.append(new_acc)
                        return new_acc
                else:
                    return 1
        else:
            return 2

    def get_account_list(self, acc_num):
        if len(self.accounts) > 0:
            for i in self.accounts:
                if i.acc_id == acc_num:
                    return i
                else:
                    return 1
        else:
            return 1

    def write_account(self, account):
        if not os.path.isfile(self.account_file):
            with open(self.account_file, "w") as acc:
                csv_write = csv.DictWriter(acc, fieldnames=self.CSV_HEADER, delimiter='|')
                csv_write.writeheader()
                csv_write.writerow(account.account_dict())
        else:
            with open(self.account_file, "a") as acc:
                csv_write = csv.DictWriter(acc, fieldnames=self.CSV_HEADER, delimiter="|")
                csv_write.writerow(account.account_dict())

    def increase_balance(self, acc_id, amount):
        acc = self.get_account(acc_id)
        if acc == 1 or acc == 2:
            return acc
        else:
            new_acc = Account(acc['Account ID'], acc['Name'])
            acc_bal = int(acc['Balance'])
            return 3

    def get_account(self, acc_id):
        """
        Takes the account ID and checks if that account is in the self.accounts list.
        If it is returns the object. If not will read the accounts files, if it finds the
        account adds it values to an Account object and appends it to self.accounts return
        the accounts object. If not found returns None
        :param acc_id:
        :return:
        """
        acc = self.get_account_list(acc_id)
        if acc is (1 or 2):
            acc_str = self.get_account_file(acc_id)
            if acc_str is (1 or 2):
                return acc_str
            else:
                acc = Account(int(acc_str['Account ID']), acc_str['Name'])
                acc.balance = int(acc_str['Balance'])
                self.accounts.append(acc)
                return acc
        else:
            return acc
