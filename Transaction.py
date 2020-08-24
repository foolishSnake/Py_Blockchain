import json


class Transaction:

    def __init__(self, from_acc, to_acc, amount, note, previous_hash):
        self.from_acc = from_acc
        self.to_acc = to_acc
        self.amount = amount
        self.note = note
        self.previous_hash = previous_hash
        self.blk_hash = None

    def set_hash(self, blk_hash):
        self.blk_hash = blk_hash

    def transaction_premine(self):
        trans_dic = {"Previous Hash": self.previous_hash, "From Account": self.from_acc,
                     "To Account": self.to_acc, "Amount": self.amount, "Note": self.note}
        trans_json = json.dumps(trans_dic)
        return trans_json


