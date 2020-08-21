import json
import csv


class Block:

    CSV_FIELDNAMES = ['Block Number', 'Block Hash', 'Nonce', 'Time Stamp', 'Creation Time', 'Block Data']

    def __init__(self, number, block_hash, time_stamp, nonce, creation_time, block_data, chain_file):
        self.number = number
        self.block_hash = block_hash
        self.nonce = nonce
        self.time_stamp = time_stamp
        self.creation_time = creation_time
        self.block_data = block_data
        self.chain_file = chain_file


    def write_block(self, block_json):

        return





