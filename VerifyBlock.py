# Application: Airgead Crypto
# File: VerifyBlock.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

import hashlib


class VerifyBlock:
    """
    Has a method to test if a block hash is valid.
    """

    def __init__(self):
        pass

    @staticmethod
    def verify_block(block_data, block_hash, block_nonce):
        """
        Verifies the work done for a mined block is correct.
        Generates a hash for block_data and block_nonce, test if the hash matches block_hash.
        Returns True or False
        :param block_data:
        :param block_hash:
        :param block_nonce:
        :return: Boolean
        """
        hashing_value = block_data + str(block_nonce)
        new_hash = hashlib.sha256(hashing_value.encode()).hexdigest()
        if new_hash == block_hash:
            return True
        else:
            return False
