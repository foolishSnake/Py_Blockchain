import hashlib


class Miner:
    """
    Miner class is used to mine new transactions on the blockchain.
    """

    def __init__(self):
        self.nonce = 0

    @staticmethod
    def get_hash(transaction, nonce):
        """
        Uses a String of transaction data and the nonce value to generate a SHA256 hash
        :param transaction:
        :param nonce:
        :return: sha_signature:
        """
        hashing_value = transaction + str(nonce)
        sha_signature = hashlib.sha256(hashing_value.encode()).hexdigest()
        return sha_signature

    @staticmethod
    def test_hash(block_hash, difficulty):
        """
        Uses a block_hash and tests if it meets the difficulty level.
        Difficulty is the number of leading 0 in the hash.
        :param block_hash:
        :return: Boolean
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
