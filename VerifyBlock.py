import hashlib


class VerifyBlock:

    def __init__(self):
        pass


    def verify_block(self, block_data, block_hash, block_nonce):
        """
        Verifies the work done for a mined block is correct.
        Generates a hash for block_data and block_nonce, test if the hash matches block_hash.
        Returns True or False
        :param block_data:
        :param block_hash:
        :param block_nonce:
        :return: Boolan
        """
        hashing_value = block_data + str(block_nonce)
        new_hash = hashlib.sha256(hashing_value.encode()).hexdigest()
        if new_hash == block_hash:
            return True
        else:
            return False

