import json
import csv
import os.path
import time


class Block:
    CSV_FIELDNAMES = "Block Number~Block Hash~Nonce~Time Stamp~Creation Time~Block Data"
    CSV_HEADER = ['Block Number', 'Block Hash', 'Nonce', 'Time Stamp', 'Creation Time', 'Block Data']


    def __init__(self, number, block_hash, time_stamp, nonce, creation_time, block_data, chain_file):
        self.number = number
        self.block_hash = block_hash
        self.nonce = nonce
        self.time_stamp = time_stamp
        self.creation_time = creation_time
        self.block_data = block_data
        self.chain_file = chain_file

    def write_block(self):
        if not os.path.isfile(self.chain_file):
            with open(self.chain_file, "w") as bc:
                csv_write = csv.DictWriter(bc, fieldnames=self.CSV_HEADER, delimiter='~')
                csv_write.writeheader()
                # csv_write.writerow(self.CSV_FIELDNAMES)
                csv_write.writerow(self.get_csv_dict())
                #bc.writelines(self.CSV_FIELDNAMES)
        else:
            with open(self.chain_file, "a") as bc:
                csv_write = csv.writer(bc, delimiter="~")
                #bc.writelines(self.get_block_csv())
                csv_write.writerow(self.get_csv_row())

        return

    def read_csv(self):
        with open(self.chain_file, 'r') as read:
            csv_read = csv.DictReader(read, delimiter="~")
            for line in csv_read:
                return line['Block Data']

    def get_block_csv(self):
        csv_line = "{}~{}~{}~{}~{}~{}".format(self.number, self.block_hash, self.time_stamp,
                                              self.nonce, self.creation_time, self.block_data)
        print("This is the line" + csv_line)
        return csv_line

    def get_csv_row(self):
        row = [str(self.number), self.block_hash, str(self.time_stamp), str(self.nonce), str(self.creation_time),
               str(self.block_data)]
        print("Row {}".format(row))

        return row
    def get_csv_dict(self):
        dict = {self.CSV_HEADER[0]: self.number, self.CSV_HEADER[1]: self.block_hash,
                self.CSV_HEADER[2]: str(self.time_stamp), self.CSV_HEADER[3]: str(self.nonce),
                self.CSV_HEADER[4]: str(self.creation_time), self.CSV_HEADER[5]: self.block_data}
        return dict


temp = "{\"Previous Block Hash\": 0, \"From Account\": 0,\"To Account\": 0, \"Amount\": 0, \"Note\": \"No note\"}"
# transaction = json.dumps(temp)
# print(transaction)

bk = Block(1, 23, time.time(), 1, 0.01, temp, "test.csv")

# bk.write_block()
trans_json = bk.read_csv()

trans_dic = json.loads(trans_json)
print(trans_json)
print(type(trans_json))
print(trans_dic["Amount"])
bk.write_block()
bk2 = Block(2, 23, time.time(), 1, 0.01, temp, "test.csv")
bk2.write_block()
