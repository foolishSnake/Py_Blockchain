# Application: Airgead Crypto
# File: BlockGUI.py
# Version: 0.1
# Author: Phillip Hourigan
# Course: DT249/4

import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tk_font
from tkinter import *
from Blockchain import Blockchain
from Account import Account
import time
import json
from datetime import datetime


class BlockGUI:

    def __init__(self):

    #     self.blockchain = blockchain
        self.blockchain = Blockchain()
        self.entry_top1 = None
        self.entry_top2 = None
        self.entry_top3 = None
        self.entry_top4 = None
        self.acc_entry = None
        self.blk_entry = None
        self.mining_entry = None
        self.output_text = None
        self.from_acc_e = None
        self.to_acc_e = None
        self.amount_e = None
        self.trans_text = None
        self.ERRORS = ["\nEmpty Input!\nPlease Enter A Valid Input!","\nSorry we could not find account ",
                        "Please Enter a Valid Block Number or Hash!", "Could Not Find Block ", "File Not Found!", "You can only enter a number!"]

    @staticmethod
    def test_account_id(blockchain, acc_id):
        """
        Take 2 parameters a Blockchain object and an int of an account ID.
        Test if the account ID is valid.
        Returns True if the account ID is valid and False id no account details are found.
        :param blockchain:
        :param acc_id:
        :return:
        """
        if not blockchain.acc_manager.get_account(acc_id):
            return False
        else:
            return True

    def input_error_int(self, string):
        """
        Takes a string as a parameter. Test if the string is a number and if its an empty string.
        If there are no errors Returns the parameter string. If there are error Returns a string given detail of the
        error.
        :param string:
        :return:
        """
        if len(string) == 0:
            return self.ERRORS[0]
        elif not string.isdigit():
            return self.ERRORS[5]
        else:
            return string
    def clear_entry(self, ent):
        """
        Take an entry object as a parameter.
        Clears all text from the entry
        :param ent:
        :return:
        """
        ent.delete(0, END)

    def update_entry(self, ent, output):
        """
        Takes 2 parameters a Entry object and the output text.
        Clears the Entry box of text and writes the output to it.
        :param ent:
        :param output:
        :return:
        """
        self.clear_entry(ent)
        ent.insert(0, output)

    def write_output_text(self, output_str):
        """
        Takes a string as parameter. Any text is the area is cleared and the parameter is writen to the
        output_text area in the GUI.
        :param output_str:
        :return:
        """
        self.output_text.delete(1.0, END)
        self.output_text.insert(1.0, output_str)

    def trans_text_write(self, entrys, output):
        """
        Takes 2 parameters list of the transaction Entrys and a String for the output text.
        Iterates over the firts 3 elements clearing the text in the fields.
        Clears the text from the last element the text area and write the ouput string to it.
        :param entrys:
        :param output:
        :return:
        """
        for i in range(3):
            self.clear_entry(entrys[i])
        self.write_trans_text(output)

    def set_difficulty(self):
        """
        Reads the value in the mining Entry. tests if there is a valid input. If input is valid updates the the
        self.difficulty attribute in the blockchain object. Gives a message saying the difficulty is updated. Displays
        the new difficulty in the mining difficulty Entry on the top of the dashboard.
        If there is an error in the input, given a meaasge detailing the issue in the output_text area.
        :return:
        """
        new_difficulty = self.mining_entry.get()
        output_srt = self.input_error_int(new_difficulty)
        if output_srt == new_difficulty:
            self.blockchain.difficulty = int(new_difficulty)
            output_srt = "\nThe Mining Difficult is set to {}".format(new_difficulty)
        self.difficulty_entry()
        self.write_output_text(output_srt)
        self.clear_entry(self.mining_entry)

    def get_blk_time(self):
        """
        This method is used to update the Entre for the time it took to create the last block on the blockchain.
        Reads the time from the Blockchain attribute last_blk_creation_time.
        Update the Entry with the last block creation time.
        :return:
        """
        blk_time = self.blockchain.last_blk_creation_time
        self.update_entry(self.entry_top3, blk_time)

    def get_avg_time(self):
        """
        This method is used to update the Average ctraetion time Entry in the GUI.
        Reads the blockchin average_cfreation_time attribute and use the data to update the Entry.
        :return:
        """
        avg_time = self.blockchain.average_creation_time
        self.update_entry(self.entry_top4, avg_time)

    def difficulty_entry(self):
        """
        Claers the text in the Entry for the minning difficulty and then updates it with the current difficulty.
        :return:
        """
        self.entry_top1.delete(0, END)
        self.entry_top1.insert(0, self.blockchain.difficulty)

    def display_acc(self):
        acc_id = self.acc_entry.get()
        self.acc_entry.delete(0, END)
        output_str = ""
        if len(acc_id) == 0:
            output_str = self.ERRORS[0] + acc_id
        elif acc_id.isdigit():
            acc = self.blockchain.acc_manager.get_account(int(acc_id))
            if not acc:
                output_str = self.ERRORS[1] + acc_id
            else:
                output_str = "Account Details\n{:12}{}\n{:12}{}\n{:12}{}"\
                    .format("Account ID:", acc.acc_id, "Name:", acc.name, "Balance:", acc.balance)
        self.write_output_text(output_str)

    def get_number_blk(self):
        """
        Read the Blockchain attribute for the last block number and add 1 to it (First block is 0).
        Use the block number to update the Number of block entry in the GUI.
        :return:
        """
        num_blk = self.blockchain.block_number + 1
        self.update_entry(self.entry_top2, num_blk)

    def display_blk(self):
        """
        Read the data entered in the Entry box for Blk / Hash.
        Tests the input to see if its a hash or block number.
        Attepts to read the blockchain file to find the block number or Hash. If found will dispaly the
        block details in the text area, if noy displays a message.
        :return:
        """
        output_str = ""
        blk = self.blk_entry.get()
        if len(blk) == 64 and (not blk.isdigit()):
            dict = self.blockchain.get_block_by_hash(blk)
            if not dict:
                output_str = self.ERRORS[3]
            else:
                output_str = self.dict_output(dict)
        elif self.input_error_int(blk) == blk:
            dict = self.blockchain.get_block_by_id(int(blk))
            if not dict:
                output_str = self.ERRORS[3]
            else:
                output_str = self.dict_output(dict)

        self.clear_entry(self.blk_entry)
        self.write_output_text(output_str)


    def dict_output(self, dict):
        """
        Takes 1 parameter a dictonary of the data in a Block.
        The dictonary data is format in a string.
        Returns a string of the formated text.
        :param dict:
        :return:
        """
        str_dict = "Block Information:\n"
        dict_trans = json.loads(dict['Block Data'])
        for key, value in dict.items():
            if key != 'Block Data':
                if key == 'Time Stamp':
                    str_dict += "{:<15}{}\n".format(key, datetime.utcfromtimestamp(float(value)))
                else:
                    str_dict += "{:<15}{}\n".format(key, value)
        print(dict_trans)
        for key, value in dict_trans.items():
            str_dict += "{:<15}{}\n".format(key, value)

        return str_dict

    def add_transaction(self):
        """
        This method is used add a new transaction on the blockchain.
        All input is tested to see if its valid. From account is tested to see if they have enough funds.
        If transaction is mined successfully and message is displayed. If there are any errors a message
        will be displayed.
        :return:
        """
        output_str = ""
        ret = False
        fields = ["From Accout ", "To Accout ", "Amount ", "Transaction Details "]
        entrys = [self.from_acc_e, self.to_acc_e, self.amount_e, self.trans_text]
        entrys_data = []
        test = entrys[0].get()
        for index, i in enumerate(entrys):
            if index < 3:
                entrys_data.append(i.get())
                temp = self.input_error_int(entrys_data[index])
                if entrys_data[index] != temp:
                    output_str += "{}{}\n".format(fields[index], temp)
                    ret = True
            else:
                entrys_data.append(i.get("1.0",END))
                if len(entrys_data[index]) == 0:
                    output_str += "{} Field Must Contain Some Text!".format(fields[index])
                    ret = True
        if ret:
            self.trans_text_write(entrys, output_str)
            return
        else:
            if int(entrys_data[0]) > self.blockchain.acc_manager.last_id:
                output_str = "We can not find the From Account {}!\n".format(entrys_data[0])
                ret = True
            elif not self.blockchain.test_funds(int(entrys_data[0]), int(entrys_data[2])):
                output_str += "Account {} Does not have the funds for this transaction!\n".format(entrys_data[0])
                ret = True
            elif int(entrys_data[1]) > self.blockchain.acc_manager.last_id:
                output_str += "We can not find the To Account {}!\n".format(entrys_data[1])
                ret = True
        if ret:
            self.trans_text_write(entrys, output_str)
            return
        else:
            if self.blockchain.create_block(int(entrys_data[0]), int(entrys_data[1]), int(entrys_data[2]),
                                         entrys_data[3]):
                output_str = "\nTransaction Mined Successfully!"
                self.trans_text_write(entrys, output_str)
                return
            else:
                output_str = "\nTransaction Failed to Mine.\nTry again"
                self.trans_text_write(entrys, output_str)
                return

    def write_trans_text(self, output):
        """
        Take 1 parameter, a String of output text.
        Clears the text area and write the output text to it.
        :param output:
        :return:
        """
        self.trans_text.delete(1.0, END)
        self.trans_text.insert(1.0, output)

    def dashboard(self):
        """
        The elements for the GUI
        :return:
        """

        root = Tk()
        root.title("Airgead Crypto Dashboard")
        font_size = tk_font.Font(size=20)

        # GUI image settings
        heading_img = PhotoImage(file=r"images/airgeadcrypto.png")
        heading = heading_img.subsample(2, 5)

        # Frame for the image
        image_frame = Frame(root)
        image_frame.grid(row=0, column=0, columnspan=8, rowspan=2)
        label_image = Label(image_frame, image=heading)
        label_image.grid(row=0, column=0, columnspan=8, rowspan=2, sticky=W+E)

        # Frame for holding all other frames in the GUI
        parent_frame = Frame(root)
        parent_frame.grid(row=3, column=0, padx=2, pady=2)

        # Frame for holding the blockchain state information
        top_frame = Frame(parent_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        top_frame.grid(row=2, column=0, columnspan=8, rowspan=2, pady=2)

        label_top1 = Label(top_frame, text="Mining Difficulty:", anchor="center")
        label_top1.grid(row=0, column=0, columnspan=2,padx=3, sticky=W+E)
        self.entry_top1 = Entry(top_frame, justify='center')
        self.entry_top1.grid(row=1, column=0, columnspan=2, sticky=W+E, padx=3, pady=2)
        self.difficulty_entry()

        label_top2 = Label(top_frame, text="Number of Blocks:", anchor="center")
        label_top2.grid(row=0, column=2, columnspan=2,padx=3)
        self.entry_top2 = Entry(top_frame, justify='center')
        self.entry_top2.grid(row=1, column=2, columnspan=2,sticky=W+E, padx=3, pady=2)
        self.get_number_blk()

        label_top3 = Label(top_frame, text="Creation time of last Block:", anchor="center")
        label_top3.grid(row=0, column=4, columnspan=2,padx=3)
        self.entry_top3 = Entry(top_frame, justify='center')
        self.entry_top3.grid(row=1, column=4, columnspan=2,sticky=W+E, padx=3, pady=2)
        self.get_blk_time()

        label_top4 = Label(top_frame, text="Average Block Creation time:", anchor="center")
        label_top4.grid(row=0, column=6, columnspan=2, padx=3)
        self.entry_top4 = Entry(top_frame, justify='center')
        self.entry_top4.grid(row=1, column=6, columnspan=2, sticky=W+E, padx=3, pady=2)
        self.get_avg_time()

        # Frame for holding the Inputs for quaring the Blockchain, changing the mining difficulty.
        large_frame = Frame(parent_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        large_frame.grid(row=4, column=0, padx=2, columnspan=8, pady=2)

        info_frame = Frame(large_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        info_frame.grid(row=0, column=0, columnspan=8, padx=3, pady=3)

        button_frame = Frame(info_frame)
        button_frame.grid(row=0, column=0, columnspan=3, padx=3, pady=3)

        heading_l = Label(button_frame, text="Quary Blockchain or Amend Mining Difficulty :", anchor=CENTER)
        heading_l.grid(row=0, column=0, pady=2, padx=2, columnspan=8)

        acc_l = Label(button_frame, text="Account No:", anchor=W)
        acc_l.grid(row=1, column=0, pady=2, padx=2, columnspan=1)
        self.acc_entry = Entry(button_frame)
        self.acc_entry.grid(row=1, column=1, columnspan=1, padx=2, pady=2)
        acc_button = Button(button_frame, text="Submit",  command=self.display_acc)
        acc_button.grid(row=1, column=2, columnspan=1,padx=2, pady=2, sticky=W,)

        mining_l = Label(button_frame, text="Mining Difficulty:", anchor=W)
        mining_l.grid(row=1, column=3, pady=2, padx=2, columnspan=1)
        self.mining_entry = Entry(button_frame)
        self.mining_entry.grid(row=1, column=4, columnspan=1, padx=2, pady=2)
        mining_button = Button(button_frame, text="Submit", command=self.set_difficulty)
        mining_button.grid(row=1, column=5, columnspan=1, padx=2, pady=2, sticky=W)

        blk_l = Label(button_frame, text="Block No. / Hash:", anchor=W)
        blk_l.grid(row=2, column=0, pady=2, padx=2, columnspan=1)
        self.blk_entry = Entry(button_frame)
        self.blk_entry.grid(row=2, column=1, columnspan=5, padx=2, pady=2, sticky=W+E)
        blk_button = Button(button_frame, text="Submit", command=self.display_blk)
        blk_button.grid(row=2, column=7, columnspan=1, padx=2, pady=2, sticky=W)

        self.output_text = Text(button_frame, height=12, width=90)
        self.output_text.grid(row=3, column=0,columnspan=8, padx=2,pady=2)

        # Frame for holding the form for adding a new transaction(Block).
        transaction_frame = Frame(large_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        transaction_frame.grid(row=3, column=0, columnspan=8, padx=3, pady=3)

        title_l = Label(transaction_frame, text="Create a New Block Transaction:", anchor=CENTER)
        title_l.grid(row=0, column=0, pady=2, padx=2, columnspan=8)

        from_acc_l = Label(transaction_frame, text="From Account:")
        from_acc_l.grid(row=1, column=0, sticky=W, columnspan=1, pady=2, padx=2)
        self.from_acc_e = Entry(transaction_frame)
        self.from_acc_e.grid(row=1, column=1, sticky=W, columnspan=1, pady=2, padx=2)

        to_acc_l = Label(transaction_frame, text="To Account:")
        to_acc_l.grid(row=1, column=2, columnspan=1, sticky=W, pady=2, padx=2)
        self.to_acc_e = Entry(transaction_frame)
        self.to_acc_e.grid(row=1, column=3, columnspan=1, sticky=W, pady=2, padx=2)

        amount_l = Label(transaction_frame, text="Transaction Amount:")
        amount_l.grid(row=1, column=4, columnspan=1, sticky=W, pady=2, padx=2)
        self.amount_e = Entry(transaction_frame)
        self.amount_e.grid(row=1, column=5, columnspan=1, sticky=W, pady=2, padx=2)

        trans_l = Label(transaction_frame, text="Enter Transaction Details:", anchor=CENTER)
        trans_l.grid(row=2, column=0, pady=2, padx=2, columnspan=8)
        self.trans_text = Text(transaction_frame, height=5, width=90)
        self.trans_text.grid(row=3, column=0, pady=2, padx=2, rowspan=3, columnspan=8, sticky=W)

        submit_b = Button(transaction_frame, text="Submit", command=self.add_transaction)
        submit_b.grid(row=6, column=0, pady=2, padx=2, columnspan=8, sticky=W + E + N + S)

        root.mainloop()

gui = BlockGUI()
gui.dashboard()
