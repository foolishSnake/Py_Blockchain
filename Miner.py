import hashlib
from VerifyBlock import VerifyBlock


class Miner:

    def __init__(self):
        self.nonce = 0

    def get_hash(self, transaction, nonce):
        """
        Uses a String of transaction data and the nonce value to generate a SHA256 hash
        :param transaction:
        :param nonce:
        :return: sha_signature:
        """
        hashing_value = transaction + str(nonce)
        sha_signature = hashlib.sha256(hashing_value.encode()).hexdigest()
        return sha_signature

    def test_hash(self, block_hash, difficulty):
        """
        Uses a block_hash and tests if it meets the difficulty level.
        Difficulty is the number of leading 0 in the hash.
        :param block_hash:
        :return: Boolan
        """
        for i in range(difficulty):
            if block_hash[i] != "0":
                # self.nonce += 1
                return False
        return True

    def mining(self, transaction, difficulty):
        """
        Calls the self.get_hash() method, test the output using the self.test_hash() method,
        Each iteration increase the self.nonce by 1 and loops until hash value passes.
        :return: [block_hash, self.nonce]
        """

        while True:
            block_hash = self.get_hash(transaction, self.nonce)
            if self.test_hash(block_hash, difficulty):
                return [block_hash, self.nonce]
            else:
                self.nonce += 1
                continue
        return block_hash


test = Miner()


hash_value = test.mining("test", 1)

print(hash_value)
print(test.nonce)

ver = VerifyBlock()
print(ver.verify_block("test", hash_value[0], hash_value[1]))

# print(test.test_hash("000637d8fcd2c6da6359e6963113a1170de795e4b725b84d1e0b4cfd9ec58ce9"))

