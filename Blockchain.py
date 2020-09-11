# Application: Airgead Crypto
# File: Blockchain.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

from Miner import Miner
from Transaction import Transaction
from VerifyBlock import VerifyBlock
from Block import Block
from AccountManager import AccountManager
import time


class Blockchain:
    NAME = "Airgead Crypto"
    block_number = 0
    difficulty = 0
    ACC_FILE = "AirgeadCryptoAccount.csv"
    BLK_FILE = "AirgeadCryptoBlockchain.csv"
    previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    blocks = []
    accounts = []

    def __init__(self):
        self.acc_manager = AccountManager(self.ACC_FILE)

    def genesis_block(self):
        """
        Creates a genesis block on the blockchain.
        Returns a string "Success" if block is created and "Error" if it falls.
        :return:
        """
        start_time = time.monotonic()
        trans = Transaction(0, 0, 1000000, "Genesis Block!", self.previous_hash).transaction_json()
        hash_data = Miner().mining(trans, self.difficulty)
        end_time = time.monotonic()
        if self. verify_hash(trans, hash_data):
            new_blk = Block(self.block_number, hash_data[0], time.time(), hash_data[1], end_time - start_time,
                            trans, self.BLK_FILE)
            self.increase_block_number()
            self.change_previous_hash(hash_data[0])
            self.blocks.append(new_blk)
            new_blk.write_block()
            return "Success"
        else:
            return "Error"

    def create_block(self, trans, blk_hash, nonce):

        return

    def first_accounts(self):
        """
        This method is used to create 3 accounts, well only be called if there is no account file.
        :return:
        """
        self.acc_manager.add_account("System")
        self.acc_manager.add_account("Alice")
        self.acc_manager.add_account("Bob")

    def add_account(self, name):
        """
        Creates a new account.
        Take a parameter of a string of a name.
        :param name:
        :return:
        """
        self.acc_manager.add_account(name)

    @staticmethod
    def verify_hash(trans, hash_data):
        """
        Test if a block hash is valid.
        Take 2 parameters trans is a string of a json of a block transaction and
        hash_data is a list the first element is the block hash the second is the block nonce.
        Returns True is the hash is valid and false if not.
        :param trans:
        :param hash_data:
        :return:
        """
        return VerifyBlock.verify_block(trans, hash_data[0], hash_data[1])

    def increase_block_number(self):
        """
        Increases the block_number attribute.
        :return:
        """
        self.block_number += 1

    def change_previous_hash(self, new_hash):
        """
        Changes the attribute for the previous hash. Value is changed after each new block is mined.
        :param new_hash:
        :return:
        """
        self.previous_hash = new_hash

bc = Blockchain()


# bc.first_accounts()
# bc.add_account("Hannah")
file = bc.acc_manager.get_account(2)
print(file.account_dict())
bc.acc_manager.amend_balance(4, 100)

# file = bc.acc_manager.get_account(2)
# print(file.account_dict())

