from Blockchain import Blockchain
from BlockGUI import BlockGUI


def main():
    bc = Blockchain()
    if test_blockchain_files(bc):
        BlockGUI(bc).dashboard()
    else:
        print("Ohh No something went wrong!")


def test_blockchain_files(blockchain):
    if blockchain.test_bc_file(blockchain.ACC_FILE) and blockchain.test_bc_file(blockchain.BLK_FILE):
        return True
    else:
        gb = blockchain.genesis_block()
        fa = blockchain.first_accounts()
        return gb and fa


if __name__ == '__main__':
    main()
