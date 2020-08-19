import json


class Block:

    def __init__(self, number, block_hash, previous_hash, time_stamp, block_data, nonce, creation_time):
        self.number = number
        self.block_hash = block_hash
        self.previous_hash = previous_hash
        self.time_stamp = time_stamp
        self.block_data = block_data
        self.nonce = nonce
        self.creation_time = creation_time

    def block_json(self):
        block_dic = {"Block Number":self.number, "Block Hash": self.block_hash, "previous_hash": self.previous_hash,
                     "Block Nonce": self.nonce, "Time Stamp":self.time_stamp, "Creation Time": self.creation_time,
                     "Block Data": self.block_data}

        block_json = json.dumps(block_dic)
        return block_dic





