# Application: Airgead Crypto
# File: Blockchain.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

import json
import csv
from Miner import Miner
from Account import Account
from Transaction import Transaction
from VerifyBlock import VerifyBlock
from Block import Block
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

    def genesis_block(self):
        """
        Creates a genesis block on the blockchain.
        Returns a string "Success" if block is created and "Error" if it falls.
        :return:
        """
        start_time = time.monotonic()
        trans = Transaction(0, 0, 1000000, "Genesis Block!", self.previous_hash).transaction()
        hash_data = Miner().mining(trans, self.difficulty)
        end_time = time.monotonic()
        if self.verity_hash(trans, hash_data):
            new_blk = Block(self.block_number, hash_data[0], time.time(), hash_data[1], end_time - start_time,
                            trans, self.BLK_FILE)
            self.increase_block_number()
            self.change_previous_hash(hash_data[0])
            self.blocks.append(new_blk)
            return "Success"
        else:
            return "Error"

    def create_block(self, trans, blk_hash, nonce):

        return

    def transaction_str(self, from_acc, to_acc, amount, note, previous_hash):
        transaction = "{\"Previous Block Hash\": previous_hash, \"From Account\": from_acc, \"To Account\": to_acc, " \
               "\"Amount\": amount, \"Note\": note} "
        return transaction

    def first_accounts(self):
        if self.last_id is None:
            sys_acc = Account("System", 1000000)
            self.last_id = 0
            self.add_account("System", 0)

            self.add_account("Alice", 100)
            self.add_account("Bob", 100)

    def verity_hash(self, trans, hash_data):
        return VerifyBlock.verify_block(trans, hash_data[0], hash_data[1])

    def increase_block_number(self):
        self.block_number += 1

    def change_previous_hash(self, new_hash):
        self.previous_hash = new_hash

