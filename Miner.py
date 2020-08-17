import hashlib

class Miner:

    def __init__(self, transaction, difficulty):
        self.transaction = transaction
        self.difficulty = difficulty
        self.nonce = 0

    def miner(self, transaction, nonce):
        hashing_value = transaction + str(nonce)
        sha_signature = hashlib.sha256(hashing_value.encode()).hexdigest()
        return sha_signature

    def test_hash(self, hash):
        for i in range(self.difficulty):
            if hash[i] != 0:
                self.nonce += 1
                return False
        return True


test = Miner("test", 0)

hash_value = test.miner("test", 0)

print(hash_value)

print(test.test_hash(hash_value))

