import json
from Miner import Miner
from Account import Account

class Blockchain:
    NAME = "Airgead Crypto"
    next_block_number = 0
    difficulty = 0
    ACC_FILE = "AirgeadCryptoAccount.json"
    BLK_FILE = "AirgeadCryptoBlockchain.json"
    previous_hash = 0000000000000000000000000000000000000000000000000000000000000000

    def genesis_block(self):
        trans = self.transaction_str(0, 0, 0, "Genesis Block\nSetup by system account", self.previous_hash)
        miner = Miner(trans, 0)
        blk_hash = ()
        genesis_dic = {"Block Number": 0, "Block Hash":}
        return None

    def create_block(self, note, from_acc, to_acc, previous_hash):
        transaction = self.transaction_str(from_acc, to_acc, note)

        return

    def transaction_str(self, from_acc, to_acc, amount, note, previous_hash):
        temp = {"Previous Block Hash": previous_hash, "From Account": from_acc,
                "To Account": to_acc, "Amount": amount, "Note": note}
        transaction = json.dumps(temp)
        return transaction

    def first_accounts(self):
        if self.last_id is None:
            sys_acc = Account("System", 1000000)
            self.last_id = 0
            self.add_account("System", 0)

            self.add_account("Alice", 100)
            self.add_account("Bob", 100)