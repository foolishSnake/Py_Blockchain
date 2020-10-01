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
        if self.mine_transaction(trans):
            self.acc_manager.amend_balance(acc.acc_id, open_balance)
            return True
        else:
            return False

    def mine_transaction(self, trans):
        """
        Takes a string of a json of a transaction. Sends the trans and the mining difficulty to the Miner object.
        Measures the time it takes for the transaction to be mined. Tests that the hash is valid.
        Added the new mined data to a Block object and writes that to the Blockchain CSV file.
        Return True on success and False it it fails.
        :param trans:
        :return:
        """
        start_time = time.monotonic()
        hash_data = Miner().mining(trans, self.difficulty)
        end_time = time.monotonic()
        if self.verify_hash(trans, hash_data):
            new_blk = Block(self.block_number + 1, hash_data[0], time.time(), hash_data[1], end_time - start_time,
                            trans, self.BLK_FILE, self.difficulty)
            self.increase_block_number()
            self.change_previous_hash(hash_data[0])
            self.blocks.append(new_blk)
            new_blk.write_block()
            return True
        else:
            return False

    def create_block(self, from_acc, to_acc, amount, note):
        """
        This method has 4 parameters, 1 is a integer for the ID of the from account, 2 is an integer for the to account,
        3 is an integer for the amount the transaction is for and 4 is a string for a note for details about
        the transaction. Tests if there is enough fund in the from account for the transaction. If there is send the
         transaction for mining. If mining is successful the balance of the To and From account are updated.
        Returns True is the method completes successfully and False if it fails.
        :param from_acc:
        :param to_acc:
        :param amount:
        :param note:
        :return:
        """
        if self.test_funds(from_acc, amount):
            trans = self.transaction_json(from_acc, to_acc, amount, note)
            if self.mine_transaction(trans):
                self.acc_manager.amend_balance(from_acc, amount * -1)
                self.acc_manager.amend_balance(to_acc, amount)
            else:
                return False
        else:
            return False
        return True
 
    def first_accounts(self):
        """
        This method is used to create 2 accounts. Both account will have be given a balance of 100
        well only be called if there is no account file.
        Returns True on success and False if it fails to added account.
        :return:
        """
        buy_in = 100
        acc_alice = self.acc_manager.add_account("Alice")
        trans_alice = self.transaction_json(1, acc_alice.acc_id, buy_in, "Buy In")
        if self.mine_transaction(trans_alice):
            self.acc_manager.amend_balance(acc_alice.acc_id, buy_in)
        else:
            return False
        acc_bob = self.acc_manager.add_account("Bob")
        trans_bob = self.transaction_json(1, acc_bob.acc_id, buy_in, "Buy In")
        if self.mine_transaction(trans_bob):
            self.acc_manager.amend_balance(acc_bob.acc_id, buy_in)
        else:
            return False

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
        """
        Take 2 parameters 1 from_acc is a integer value for the ID of the from account and 2 amount the integer value
        for the transaction. The amount is test against the balance of the account to see if there is enough funds for
        the transaction.
        Returns True if there is enough funds and False if there is not enough.
        :param from_acc:
        :param amount:
        :return:
        """
        if self.acc_manager.get_account(from_acc).balance >= amount:
            return True
        else:
            return False

    def get_block_by_id(self, blk_num):
        """
        Take 1 parameter blk_num, this is an integer value of the block ID
        Searches the Blockchain file for the block data of a block number.
        Returns a string for the block information on success or None if it fails.
        :param blk_num:
        :return:
        """
        data = self.read_blk('Block Number', blk_num)
        return data

    def get_block_by_hash(self, blk_hash):
        """
        Take 1 parameter blk_num, this is an string of the block hash.
        Searches for a block in the Blockchain file using its hash value.
        Returns a string of the block data on success or None if it fails.
        :param blk_hash:
        :return:
        """
        data = self.read_blk('Block Hash', blk_hash)
        return data

    def read_blk(self, key, value):
        """
        Takes 2 parameters, a string of the Key and the value to be searched for.
        Reads the lines in the blockchain file, search for a Block using its key value pair.
        Returns a dictionary for the line if found, None if data not found or if the blockchain file was not found.
        :param key:
        :param value:
        :return:
        """
        if os.path.isfile(self.BLK_FILE):
            with open(self.BLK_FILE, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    if int(line[key]) == value:
                        return line
                else:
                    return None
        else:
            return None

    @staticmethod
    def test_bc_file(file):
        """
        Takes a string of a path to file for the blockchain storage file:
        Test if there is a file at the path.
        Returns True if the file is found and False if not.
        :param file:
        :return:
        """
        if os.path.isfile(file):
            return True
        else:
            return False

    @staticmethod
    def test_bc_file_data(file):
        """
        Takes a string of a path to file for the blockchain storage file:
        Test if there is a any data in the file at the path.
        Returns True if the file there is data in the file and False if file is empty.
        :param file:
        :return:
        """
        if os.path.getsize(file) != 0:
            return True
        else:
            return False

    def set_block_number(self):
        """
        This method is used to set the block number in the Class.
        It attempts it tests if the blockchain file exists and if there is any data in it.
        If there the file exists and it has data the self.block_number attribute is with the value of the
        last block added. If there is no blockchain data the attribute is set to 0.
        :return:
        """
        block_number = 0
        if self.test_bc_file(self.BLK_FILE) and self.test_bc_file_data(self.BLK_FILE):
            with open(self.BLK_FILE, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    block_number = int(line["Block Number"])
                    pre_hash = line["Block Hash"]
                self.block_number = block_number
                self.previous_hash = pre_hash
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
                self.average_creation_time = average_time / (self.block_number + 1)
        else:
            self.average_creation_time = average_time
