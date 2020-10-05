from Blockchain import Blockchain
from BlockGUI import BlockGUI


def main():
    """
    Main instantiates a Blockchain object. When created tests if there is an account and blockchain .csv
    file. If there is starts the GUI dashboard. If the files are not created, set up default accounts and
    a genesis block.
    :return:
    """
    bc = Blockchain()
    if test_blockchain_files(bc):
        BlockGUI(bc).dashboard()
    else:
        bc.genesis_block()
        bc.first_accounts()
        BlockGUI(bc).dashboard()

def test_blockchain_files(blockchain):
    """
    Take a  Blockchain object as a parameter.
    Tests if the Blockchain account and Block file exist and id they are empty.
    If they don't exist creates a genesis block and a system account plus two user accounts.
    Returns True if the files exist and there is data in them and True if it creates the genesis block and
    default accounts.
    Returns False if it fails to create the genesis block our account.
    :param blockchain:
    :return:
    """
    if blockchain.test_bc_file(blockchain.ACC_FILE) and blockchain.test_bc_file(blockchain.BLK_FILE):
        return True
    else:
        gb = blockchain.genesis_block()
        fa = blockchain.first_accounts()
        return gb and fa


if __name__ == '__main__':
    main()
