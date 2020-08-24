# Application: Airgead Crypto
# File: Block.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

import csv
import os.path


class Block:
    CSV_HEADER = ['Block Number', 'Block Hash', 'Nonce', 'Time Stamp', 'Creation Time', 'Block Data']

    def __init__(self, number, block_hash, time_stamp, nonce, creation_time, block_data, chain_file):
        self.number = number
        self.block_hash = block_hash
        self.nonce = nonce
        self.time_stamp = time_stamp
        self.creation_time = creation_time
        self.block_data = block_data
        self.chain_file = chain_file

    def write_block(self):
        """
        Writes the data for a block to a .csv file, using the "|" as the delimiter.
        Test if the file exists, if not creates a new file.
        If the file exists it appends the new block data to the file.
        :return:
        """
        if not os.path.isfile(self.chain_file):
            with open(self.chain_file, "w") as bc:
                csv_write = csv.DictWriter(bc, fieldnames=self.CSV_HEADER, delimiter='|')
                csv_write.writeheader()
                csv_write.writerow(self.get_csv_dict())
        else:
            with open(self.chain_file, "a") as bc:
                csv_write = csv.writer(bc, delimiter="|")
                csv_write.writerow(self.get_csv_dict())

        return

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
        Returns the line if found, "Data Not Found!" message if not found and ""Can't find Blockchain file"
        message if if can't find the blockchain file.
        :param key:
        :param value:
        :return:
        """
        if os.path.isfile(self.chain_file):
            with open(self.chain_file, 'r') as read:
                csv_read = csv.DictReader(read, delimiter="|")
                for line in csv_read:
                    if line[key] == value:
                        return line
                    else:
                        return "Data Not Found!"
        else:
            return "Can't find Blockchain file \"{}\"".format(self.chain_file)

    def get_csv_dict(self):
        """
        Creates a dictionary of the key value pairs of the class attributes. Returns the dictionary.
        :return:
        """
        csv_dict = {self.CSV_HEADER[0]: self.number, self.CSV_HEADER[1]: self.block_hash,
                    self.CSV_HEADER[2]: str(self.time_stamp), self.CSV_HEADER[3]: str(self.nonce),
                    self.CSV_HEADER[4]: str(self.creation_time), self.CSV_HEADER[5]: self.block_data}
        return csv_dict
