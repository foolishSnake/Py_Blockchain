from Account import Account
import os.path
import csv


class AccountManager:
    accounts = []
    last_id = 0
    CSV_HEADER = ['Account ID', 'Name', 'Balance']

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
                return "Account ID retrieved"

        else:
            return "Can't find Blockchain file \"{}\"".format(self.account_file)

    def get_account(self, acc_num):
        if os.path.isfile(self.account_file):
            with open(self.account_file, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                   if line['Account ID'] == acc_num:
                        return line
                else:
                    return "Data Not Found!"
        else:
            return "Can't find Accounts file \"{}\"".format(self.account_file)

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
        if acc != "Data Not Found!" or acc != "Can't find Blockchain file \"{}\"".format(self.account_file)
            new_acc = Account(acc['Account ID'], acc['Name'])
            acc_bal = int(acc['Balance'])

