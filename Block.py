class Block:

    number = None
    hash = None
    previous_hash = None
    time_stamp = None
    block_data = None
    nonce = None

    def __init__(self, number, hash, previous_hash, time_stamp, block_data, nonce, creation_time):
        self.number = number
        self.hash = hash
        self.previous_hash = previous_hash
        self.time_stamp = time_stamp
        self.block_data = block_data
        self.nonce = nonce
        self.creation_time = creation_time



