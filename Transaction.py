# Author: Phillip Hourigan
# Course: DT249/4
# Version: 0.1
import json


class Transaction:

    def __init__(self, from_acc, to_acc, amount, note, previous_hash):
        """
        A data structure for hold the transaction data of the Blockchain.
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

    def transaction(self):
        """
        Creates a string for a JSON of the transaction data.
        Returns a String of the JSON data.
        :return:
        """
        trans_dic = {"Previous Hash": self.previous_hash, "From Account": self.from_acc,
                     "To Account": self.to_acc,"Amount": self.amount,"Note": self.note}
        trans_json = json.dumps(trans_dic)

        return trans_json


tran = Transaction(10, 555, 1,  "Payment for stuff", "100000")
print(tran.transaction())