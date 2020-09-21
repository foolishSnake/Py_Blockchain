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
    difficulty = 1
    average_creation_time = 0.0
    last_blk_creation_time = 0.0
    ACC_FILE = "AirgeadCryptoAccount.csv"
    BLK_FILE = "AirgeadCryptoBlockchain.csv"
    previous_hash = "0000000000000000000000000000000000000000000000000000000000000000"
    blocks = []
    accounts = []

    def __init__(self):
        self.acc_manager = AccountManager(self.ACC_FILE)
        self.set_block_number()
        self.set_average_time()

    def genesis_block(self):
        """
        Creates a genesis block on the blockchain.
        Returns True if Successful, False it it fails.
        :return:
        """
        open_balance = 1000000
        acc = self.acc_manager.add_account("System")
        trans = self.transaction_json(acc.acc_id, acc.acc_id, open_balance, "Genesis Block!")
        if self.mine_transaction(trans) == "Success":
            self.acc_manager.amend_balance(acc.acc_id, open_balance)
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

    def create_block(self, from_acc, to_acc, amount, note):
        if self.test_funds(from_acc, amount):
            trans = self.transaction_json(from_acc, to_acc, amount, note)
            if self.mine_transaction(trans) == "Success":
                self.acc_manager.amend_balance(from_acc, amount * -1)
                self.acc_manager.amend_balance(to_acc, amount)
            else:
                return 5
        else:
            return 4
 
    def first_accounts(self):
        """
        This method is used to create 2 accounts. Both account will have be given a balance of 100
        well only be called if there is no account file.

        :return:
        """
        buy_in = 100
        acc_alice = self.acc_manager.add_account("Alice")
        trans_alice = self.transaction_json(1, acc_alice.acc_id, buy_in, "Buy In")
        if self.mine_transaction(trans_alice) == "Success":
            self.acc_manager.amend_balance(acc_alice.acc_id, buy_in)
        acc_bob = self.acc_manager.add_account("Bob")
        trans_bob = self.transaction_json(1, acc_bob.acc_id, buy_in, "Buy In")
        if self.mine_transaction(trans_bob) == "Success":
            self.acc_manager.amend_balance(acc_bob.acc_id, buy_in)

        return True

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

    @staticmethod
    def test_bc_file(file):
        if os.path.isfile(file):
            return True
        else:
            return False

    @staticmethod
    def test_bc_file_data(file):
        if os.path.getsize(file) != 0:
            return True
        else:
            return False

    def set_block_number(self):
        block_number = 0
        if self.test_bc_file(self.BLK_FILE) and self.test_bc_file_data(self.BLK_FILE):
            with open(self.BLK_FILE, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    block_number = int(line["Block Number"])
                self.block_number = block_number
        else:
            self.block_number = block_number

    def set_average_time(self):
        """
        Attempts to read the blockchain file to find the average creation time of a block.
        Set the attribute self.average_creation_time with the mean.
        :return:
        """
        average_time = 0.0
        if self.test_bc_file(self.BLK_FILE) and self.test_bc_file_data(self.BLK_FILE):
            with open(self.BLK_FILE, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    average_time += float(line["Creation Time"])
                    self.last_blk_creation_time = float(line["Creation Time"])
                self.average_creation_time = average_time / self.block_number
        else:
            self.average_creation_time = average_time



# bc = Blockchain()
# # print(bc.transaction_json(1,2, 100, "Note ya"))
# bc.genesis_block()
# bc.first_accounts()
# bc.create_block(2, 4, 50, "Sale of Car.")

# # bc.first_accounts()
# # bc.add_account("Hannah")
# file = bc.acc_manager.get_account(2)
# print(file.account_dict())
# bc.acc_manager.amend_balance(4, 100)
#
# # file = bc.acc_manager.get_account(2)
# # print(file.account_dict())

