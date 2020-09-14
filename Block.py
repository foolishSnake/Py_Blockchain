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
            with open(self.chain_file, "w", newline='') as bc:
                csv_write = csv.DictWriter(bc, fieldnames=self.CSV_HEADER, delimiter='|')
                csv_write.writeheader()
                csv_write.writerow(self.get_csv_dict())
        else:
            with open(self.chain_file, "a", newline='') as bc:
                csv_write = csv.writer(bc, delimiter="|")
                csv_write.writerow(self.get_csv_dict())

        return

    def get_csv_dict(self):
        """
        Creates a dictionary of the key value pairs of the class attributes. Returns the dictionary.
        :return:
        """
        csv_dict = {self.CSV_HEADER[0]: self.number, self.CSV_HEADER[1]: self.block_hash,
                    self.CSV_HEADER[2]: str(self.nonce), self.CSV_HEADER[3]: str(self.time_stamp),
                    self.CSV_HEADER[4]: str(self.creation_time), self.CSV_HEADER[5]: self.block_data}
        return csv_dict
