# Application: Airgead Crypto
# File: Account.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

class Account:
    """
    Account class is used as a data structure for a user account.
    Has methods to set the balance and return a dictionary with the account attributes.
    """

    def __init__(self, acc_id, name):
        """
        Takes a integer for the acc_id and a string for the account name as parameters.
        Set the balance attribute to 0, balance can only be added using a mined transaction.
        :param acc_id:
        :param name:
        """
        self.name = name
        self.acc_id = acc_id
        self.balance = 0

    def set_balance(self, amount):
        """
        Takes a value the the balance has to be increased or decreased by.
        Decreased amount are sent as negative values.
        :param amount:
        :return:
        """
        self.balance += amount

    def account_dict(self):
        """
        Returns a Dictionary object with the Account objects attributes.
        :return:
        """
        acc_dict = {'Account ID': self.acc_id, 'Name': self.name, 'Balance': self.balance}
        return acc_dict
