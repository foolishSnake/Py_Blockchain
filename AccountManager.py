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
            print("Account has accounts in it")
            for i in self.accounts:
                if i.acc_id == acc_num:
                    print("found account")
                    return i
            print("cant find account")
            return 1
        else:
            print("there are no records in the account list")
            return 1

    def write_account(self, account):
        if not os.path.isfile(self.account_file):
            with open(self.account_file, "w", newline='') as acc:
                csv_write = csv.DictWriter(acc, fieldnames=self.CSV_HEADER, delimiter='|')
                csv_write.writeheader()
                csv_write.writerow(account.account_dict())
        else:
            with open(self.account_file, "a", newline='') as acc:
                csv_write = csv.DictWriter(acc, fieldnames=self.CSV_HEADER, delimiter="|")
                if os.path.getsize(self.account_file) == 0:
                    csv_write.writeheader()
                csv_write.writerow(account.account_dict())


    def amend_balance(self, acc_id, amount):
        """
        Has the account ID and amount the balance has to be changed by as parameters. Use the acc_id to get an Account
        object. Amend the account balance. On success returns an updated Account object.
        Returns 1 if the acc_id was not found, 2 if the account csv file was not found.
        :param acc_id:
        :param amount:
        :return:
        """
        acc = self.get_account(acc_id)
        if acc == 1 or acc == 2:
            return acc
        else:
            acc.balance += amount
            return acc

    def get_account(self, acc_id):
        """
        Takes the account ID and checks if that account is in the self.accounts list.
        If it is returns the object. If not, will attempt to read the accounts files, if it finds the
        account adds it values to an Account object and appends it to self.accounts return
        the accounts object. Returns 1 if account is not found and 2 if account file is not found.
        :param acc_id:
        :return:
        """
        acc_list = self.get_account_list(acc_id)
        if acc_list is (1 or 2):
            acc_list = self.get_account_file(acc_id)
            return acc_list
        else:
            return acc_list

    def update_csv(self, acc_id, amount):
        """
        The read write part of this code is an amendment of Stack Overflow user Adam Smith answer
        https://stackoverflow.com/questions/28416678/python-replacing-value-of-a-row-in-a-csv-file
        :param acc_id:
        :param amount:
        :return:
        """
        acc = self.get_account(acc_id)
        if not os.path.isfile(self.account_file):
            return 2
        else:
            if type(acc) == Account:
                acc.set_balance(amount)
                output = []
                with open(self.account_file) as in_file:
                    reader = csv.DictReader(in_file, delimiter='|')
                    for line in reader:
                        print(line)
                        if int(line['Account ID']) == acc_id:
                            output.append(acc.account_dict())
                        else:
                            output.append(line)

                with open(self.account_file, 'w', newline='') as out_file:
                    writer = csv.DictWriter(out_file, delimiter='|', fieldnames=self.CSV_HEADER)
                    writer.writeheader()
                    writer.writerows(output)


            #     with open(self.account_file, 'w', newline='') as out_file:
            #         writer = csv.DictWriter(out_file, delimiter='|', fieldnames=self.CSV_HEADER)
            #         try:
            #             writer.writeheader()
            #             for line in reader:
            #                 # print(int(line[0]) == 4)
            #                 if int(line[self.CSV_HEADER[0]]) == acc_id:
            #                     print(line)
            #                     writer.writerow(acc.account_dict())
            #                 else:
            #                     writer.writerow(line)
            #             writer.writerows(reader)
            #         except ValueError:
            #             writer.writerows(reader)
            #             return 1
            #
            #     return 3
            # else:
            #     return acc

# acc_man = AccountManager("AirgeadCryptoAccount.csv")
#
# val = acc_man.update_csv(1, 100)
# # print(acc_man.ERROR_CODES[val])
