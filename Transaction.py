# Application: Airgead Crypto
# File: Transaction.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

import json


class Transaction:
    """
    Transaction class has the attributes need for a transaction on the blockchain.
    """

    def __init__(self, from_acc, to_acc, amount, note, previous_hash):
        """
        Take the parameters from_acc integer, to_acc integer, amount integer,
        previous_hash string of a SHA 256 bit hash.
        Has methods to set the block hash after mining, create a json of the transaction data.
        :param from_acc:
        :param to_acc:
        :param amount:
        :param note:
        :param previous_hash:
        """
        self.from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount
        self.note = note
        self.previous_hash = previous_hash
        self.blk_hash = None

    def set_hash(self, blk_hash):
        """
        Sets the attribute value for the block hash.
        :param blk_hash:
        :return:
        """
        self.blk_hash = blk_hash

    def transaction_json(self):
        """
        Returns a string of a json with the key value pairs of the transaction attributes.
        :return:
        """
        trans_dic = {"Previous Hash": self.previous_hash, "From Account": self.from_acc,
                     "To Account": self.to_acc, "Amount": self.amount, "Note": self.note}
        trans_json = json.dumps(trans_dic)
        return trans_json
