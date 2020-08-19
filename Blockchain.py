import json

class Blockchain:
    NAME = "Airgead Crypto"
    next_block_number = 0
    difficulty = 0
    ACC_FILE = "AirgeadCryptoAccount.json"
    BLK_FILE = "AirgeadCryptoBlockchain.json"

    def genesis_block(self):
        return None

    def create_block(self, note, from_acc, to_acc):
        transaction = self.transaction_str(from_acc, to_acc, note)

        return

    def transaction_str(self, from_acc, to_acc, amount, note):
        temp = {"From Account": from_acc, "To Account": to_acc, "Amount": amount, "Note": note}
        transaction = json.dumps(temp)
        return transaction
