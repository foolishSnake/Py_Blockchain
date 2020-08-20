import json


class Block:

    def __init__(self, number, block_hash, time_stamp, nonce, creation_time, block_data, chain_file):
        self.number = number
        self.block_hash = block_hash
        self.nonce = nonce
        self.time_stamp = time_stamp
        self.creation_time = creation_time
        self.block_data = block_data
        self.chain_file = chain_file

    def block_json(self):
        block_dic = {"Block Number": self.number, "Block Hash": self.block_hash, "Block Nonce": self.nonce,
                     "Time Stamp": self.time_stamp, "Creation Time": self.creation_time, "Block Data": self.block_data}

        block_json = json.dumps(block_dic)
        return block_json

    def write_block(self, block_json):
        return





