# Application: Airgead Crypto
# File: Blockchain.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

from Miner import Miner
from VerifyBlock import VerifyBlock
from Block import Block
from AccountManager import AccountManager
import time
import json
import os
import csv


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
        Returns True if Successful, False it it fails.
        :return:
        """
        trans = self.transaction_json(1, 1, 1000000, "Genesis Block!")
        if self.mine_transaction(trans) == "Success":
            self.acc_manager.amend_balance(1, 1000000)
            return True
        else:
            return False

    def mine_transaction(self, trans):
        start_time = time.monotonic()
        hash_data = Miner().mining(trans, self.difficulty)
        end_time = time.monotonic()
        if self.verify_hash(trans, hash_data):
            new_blk = Block(self.block_number, hash_data[0], time.time(), hash_data[1], end_time - start_time,
                            trans, self.BLK_FILE)
            self.increase_block_number()
            self.change_previous_hash(hash_data[0])
            self.blocks.append(new_blk)
            new_blk.write_block()
            return "Success"
        else:
            return "Error"


    def create_block(self, trans):

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

    def transaction_json(self, from_acc, to_acc, amount, note):
        """
        Takes 4 parameters. 1 is an integer for the from account, 2 an integer for to account,
        3, integer for a value of the transaction and 4 string for the note.
        Returns a string of a json of the transaction data.
        :param from_acc:
        :param to_acc:
        :param amount:
        :param note:
        :return:
        """
        trans_json = json.dumps({"Previous Hash": self.previous_hash, "From Account": from_acc,
                                 "To Account": to_acc, "Amount": amount, "Note": note})
        return trans_json

    def test_funds(self, from_acc, amount):
        if self.acc_manager.get_account(from_acc).balance >= amount:
            return True
        else:
            return False

    def get_block_by_id(self, blk_num):
        """
        Searches the Blockchain file for the block data of a block number.
        :param blk_num:
        :return:
        """
        data = self.read_blk('Block Number', blk_num)
        return data

    def get_block_by_hash(self, blk_hash):
        """
        Searches for a block in the Blockchain file using its hash value.
        :param blk_hash:
        :return:
        """
        data = self.read_blk('Block Hash', blk_hash)
        return data

    def read_blk(self, key, value):
        """
        Reads the lines in the blockchain file, search for a Block using its key value pair.
        Returns the line if found, 1 if data not found and 2 if the blockchain file wa not found.
        :param key:
        :param value:
        :return:
        """
        if os.path.isfile(self.BLK_FILE):
            with open(self.BLK_FILE, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    if line[key] == value:
                        return line
                    else:
                        return 1
        else:
            return 2

bc = Blockchain()
# print(bc.transaction_json(1,2, 100, "Note ya"))
bc.genesis_block()

# # bc.first_accounts()
# # bc.add_account("Hannah")
# file = bc.acc_manager.get_account(2)
# print(file.account_dict())
# bc.acc_manager.amend_balance(4, 100)
#
# # file = bc.acc_manager.get_account(2)
# # print(file.account_dict())

