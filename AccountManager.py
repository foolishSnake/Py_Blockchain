# Application: Airgead Crypto
# File: AccountManager.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

from Account import Account
import os.path
import csv


class AccountManager:
    """
    Account Manager is used to manage the interaction with Account objects and the storage file.
    """
    accounts = []
    last_id = 0
    CSV_HEADER = ['Account ID', 'Name', 'Balance']
    ERROR_CODES = {1: "Record Not Found", 2: "File Not Found", 3: "Success"}

    def __init__(self, account_file):
        """
        Takes a string for the account file as a parameter, use it to set the account_file attribute.
        Calls the self.get_last_id() method to set the value of the last_id attribute.
        :param account_file:
        """
        self.account_file = account_file
        self.get_last_id()

    def add_account(self, name):
        """
        Take the name of the account holder and creates a new Account object for it,
        adds the object to the accounts list. Call the write_account method to save the details to file.
        Increases the last_id attribute by one.
        Returns the account object on completion.
        :param name:
        :return:
        """
        new_acc = Account(self.last_id + 1, name)
        self.accounts.append(new_acc)
        self.last_id += 1
        self.write_account(new_acc)

        return new_acc

    def get_last_id(self):
        """
        Attempts to read the account csv file to get the value of the last account ID used.
        If found sets the self.last_id attribute.
        Returns None if it fails to read the file.
        :return:
        """
        if os.path.isfile(self.account_file):
            with open(self.account_file, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    self.last_id = int(line['Account ID'])
                return None

        else:
            return None

    def get_account_file(self, acc_num):
        """
        Takes an integer value for the account ID, searches the account file for the account.
        If successful returns a Account object with account details and adds it to the accounts list.
        If it fails will return None if it can't find the account or can't find the file.
        :param acc_num:
        :return:
        """
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
                    return None
        else:
            return None

    def get_account_list(self, acc_num):
        """
        Takes the account ID as a parameter and searches the accounts file list to find the account object.
        On success returns an account object, if it falls to find the account returns None
        :param acc_num:
        :return:
        """
        if len(self.accounts) > 0:
            for i in self.accounts:
                if i.acc_id == acc_num:
                    return i
        else:
            return None

    def write_account(self, account):
        """
        Takes an account object as a parameter, attempts to write the account details to the csv file.
        If it can't find the file will create a new file a added the account details to it.
        If it finds the file will append the details to the end of the file.
        The csv file use '|' as its delimiter.
        :param account:
        :return:
        """
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
        Takes the  account ID and amount the balance has to be changed by as parameters.
        Use the acc_id to get an Account object.
        Amend the account balance. On success returns an updated Account object.
        Returns None if the acc_id was not found or account csv file was not found.
        :param acc_id:
        :param amount:
        :return:
        """
        acc = self.get_account(acc_id)
        if not acc:
            return None
        else:
            acc.set_balance(amount)
            self.update_csv(acc)
            return acc

    def get_account(self, acc_id):
        """
        Takes the account ID and checks if that account is in the self.accounts list.
        If it is returns the object. If not, will attempt to read the accounts files, if it finds the
        account adds it values to an Account object and appends it to self.accounts return
        the accounts object. Returns None if account is  or file is not found.
        :param acc_id:
        :return:
        """
        acc_list = self.get_account_list(acc_id)
        if not acc_list:
            acc_list = self.get_account_file(acc_id)
            if not acc_list:
                return None
        else:
            return acc_list

    def update_csv(self, acc):
        """
        Takes an Account object and uses it to update the balance in the account csv file.
        The read write part of this code is an amendment of Stack Overflow user Adam Smith answer
        https://stackoverflow.com/questions/28416678/python-replacing-value-of-a-row-in-a-csv-file
        :param acc:
        :return:
        """
        if not os.path.isfile(self.account_file):
            return None
        else:
            if type(acc) == Account:
                output = []
                with open(self.account_file) as in_file:
                    reader = csv.DictReader(in_file, delimiter='|')
                    for line in reader:
                        if int(line['Account ID']) == acc.acc_id:
                            output.append(acc.account_dict())
                        else:
                            output.append(line)
                with open(self.account_file, 'w', newline='') as out_file:
                    writer = csv.DictWriter(out_file, delimiter='|', fieldnames=self.CSV_HEADER)
                    writer.writeheader()
                    writer.writerows(output)
            else:
                return None
