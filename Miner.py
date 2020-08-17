import hashlib


class Miner:

    def __init__(self, transaction, difficulty):
        self.transaction = transaction
        self.difficulty = difficulty
        self.nonce = 0

    def get_hash(self, transaction, nonce):
        hashing_value = transaction + str(nonce)
        sha_signature = hashlib.sha256(hashing_value.encode()).hexdigest()
        return sha_signature

    def test_hash(self, hash):
        for i in range(self.difficulty):
            if hash[i] != 0:
                self.nonce += 1
                return False
        return True

    def mining(self):

        while True:
            block_hash = self.get_hash(self.transaction, self.nonce)
            if self.test_hash(block_hash):
                return [block_hash, self.nonce]
            else:
                self.nonce += 1
                continue
        return block_hash


test = Miner("test", 1)

hash_value = test.mining()

print(hash_value)

print(test.test_hash(hash_value))

