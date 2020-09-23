import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tk_font
from tkinter import *
from Blockchain import Blockchain
from Account import Account
import time


class BlockGUI:

    def __init__(self):

    #     self.blockchain = blockchain
        self.blockchain = Blockchain()
        self.acc_entry = None
        self.blk_entry = None
        self.mining_entry = None
        self.output_text = None
        self.from_acc_e = None
        self.to_acc_e = None
        self.amount_e = None
        self.trans_text = None
        self.ERRORS = ["\nEmpty Input!\nPlease Enter A Valid Input!","\nSorry we could not find account ",
                        "Please Enter a Valid Blocknumber!", "Could Not Find Block ", "File Not Found!"]

    @staticmethod
    def test_account_id(blockchain, acc_id):
        if blockchain.acc_manager.get_account(acc_id) is (1 or 2):
            return False
        else:
            return True

    def display_acc(self):
        acc_id = self.acc_entry.get()
        self.acc_entry.delete(0, END)
        output_str = ""
        if len(acc_id) == 0:
            output_str = self.ERRORS[0] + acc_id
        elif acc_id.isdigit():
            acc = self.blockchain.acc_manager.get_account(int(acc_id))
            if acc is (1 or 2):
                output_str = self.ERRORS[1] + acc_id
            else:
                output_str = "Account Details\n{:15}{}\n{:15}{}\n{:15}{}"\
                    .format("Account ID:", acc.acc_id, "Name:", acc.name, "Balance:", acc.balance)
        self.output_text.delete(1.0, END)
        self.output_text.insert(1.0, output_str)

    def display_blk(self):
        blk = self.blk_entry.get()
        output_str = ""
        if len(blk) == 0:
            output_str = self.ERRORS[0]
        elif blk.isdigit():
            if int(blk) > self.blockchain.block_number:
                output_str = self.ERRORS[3]
        else:
            blk_data = self.blockchain.get_block_by_id(int(blk))
            if blk_data == 1:
                output_str = self.ERRORS[3] + blk
            elif blk_data == 2:
                output_str = self.ERRORS[4]
            else:
                output_str = "".format(blk_data['Block Number'], blk_data['Block Hash'], blk_data['Nonce'],
                                       time.ctime(blk_data['Time Stamp']), )



    def dashboard(self):

        root = Tk()
        root.title("Airgead Crypto Dashboard")
        font_size = tk_font.Font(size=20)

        heading_img = PhotoImage(file=r"images/airgeadcrypto.png")
        heading = heading_img.subsample(2, 5)

        image_frame = Frame(root)
        image_frame.grid(row=0, column=0, columnspan=8, rowspan=2)
        label_image = Label(image_frame, image=heading)
        label_image.grid(row=0, column=0, columnspan=8, rowspan=2, sticky=W)

        parent_frame = Frame(root)
        parent_frame.grid(row=3, column=0, padx=2, pady=2)

        top_frame = Frame(parent_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        top_frame.grid(row=2, column=0, columnspan=8, rowspan=2, pady=2)

        label_top1 = Label(top_frame, text="Mining Difficulty:", anchor="center")
        label_top1.grid(row=0, column=0, columnspan=2,padx=3)
        entry_top1 = Entry(top_frame, justify='center')
        entry_top1.grid(row=1, column=0, columnspan=2, sticky=W+E, padx=3, pady=2)
        entry_top1.delete(0, END)
        entry_top1.insert(0, self.blockchain.difficulty)

        label_top2 = Label(top_frame, text="Number of Blocks:", anchor="center")
        label_top2.grid(row=0, column=2, columnspan=2,padx=3)
        entry_top2 = Entry(top_frame, justify='center')
        entry_top2.grid(row=1, column=2, columnspan=2,sticky=W+E, padx=3, pady=2)
        entry_top2.delete(0, END)
        entry_top2.insert(0, (self.blockchain.block_number + 1))

        label_top3 = Label(top_frame, text="Creation time of last Block:", anchor="center")
        label_top3.grid(row=0, column=4, columnspan=2,padx=3)
        entry_top3 = Entry(top_frame, justify='center')
        entry_top3.grid(row=1, column=4, columnspan=2,sticky=W+E, padx=3, pady=2)
        entry_top3.delete(0, END)
        entry_top3.insert(0, self.blockchain.last_blk_creation_time)

        label_top4 = Label(top_frame, text="Average Block Creation time:", anchor="center")
        label_top4.grid(row=0, column=6, columnspan=2, padx=3)
        entry_top4 = Entry(top_frame, justify='center')
        entry_top4.grid(row=1, column=6, columnspan=2, sticky=W+E, padx=3, pady=2)
        entry_top4.delete(0, END)
        entry_top4.insert(0, self.blockchain.average_creation_time)

        large_frame = Frame(parent_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        large_frame.grid(row=4, column=0, padx=2, columnspan=8, pady=2)

        info_frame = Frame(large_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        info_frame.grid(row=0, column=0, columnspan=8, padx=3, pady=3)

        button_frame = Frame(info_frame)
        button_frame.grid(row=0, column=0, columnspan=3, padx=3, pady=3)

        acc_button = Button(button_frame, text="Display Account details:",  command=self.display_acc)
        acc_button.grid(row=0, column=0, columnspan=2,padx=2, pady=2, sticky="ew",)
        self.acc_entry = Entry(button_frame)
        self.acc_entry.grid(row=1, column=0, columnspan=2, padx=2, pady=2)

        blk_button = Button(button_frame, text="Get BLK by Number:")
        blk_button.grid(row=0, column=2, columnspan=2, padx=2, pady=2, sticky="ew")
        self.blk_entry = Entry(button_frame)
        self.blk_entry.grid(row=1, column=2, columnspan=2, padx=2, pady=2)

        blk_button = Button(button_frame, text="Get BLK by Hash:")
        blk_button.grid(row=0, column=4, columnspan=2, padx=2, pady=2, sticky="ew")
        self.blk_entry = Entry(button_frame)
        self.blk_entry.grid(row=1, column=4, columnspan=2, padx=2, pady=2)

        mining_button = Button(button_frame, text="Set Mining difficulty")
        mining_button.grid(row=0, column=6, columnspan=2, padx=2, pady=2, sticky="ew")
        self.mining_entry = Entry(button_frame)
        self.mining_entry.grid(row=1, column=6, columnspan=2, padx=2, pady=2)

        self.output_text = Text(button_frame, height=12, width=90)
        self.output_text.grid(row=2, column=0,columnspan=8, padx=2,pady=2)

        transaction_frame = Frame(large_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        transaction_frame.grid(row=3, column=0, columnspan=8, padx=3, pady=3)

        title_l = Label(transaction_frame, text="Create a New Block Transaction:", anchor=CENTER)
        title_l.grid(row=0, column=0, pady=2, padx=2, columnspan=8)
        # title_e = Entry(t_gui)
        # title_e.grid(row=1, column=1, sticky=W, pady=2, padx=2)

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
        self.trans_text = Text(transaction_frame, height=8, width=90)
        self.trans_text.grid(row=3, column=0, pady=2, padx=2, rowspan=3, columnspan=8, sticky=W)

        submit_b = Button(transaction_frame, text="Submit")
        submit_b.grid(row=6, column=0, pady=2, padx=2, columnspan=8, sticky=W + E + N + S)

        root.mainloop()

gui = BlockGUI()
gui.dashboard()


    # lable_num_blk = Label(root, text="Number of blocks - {}".format(0))
    # lable_num_blk['font'] = font_size
    #
    #
    # lable_last_blk_time = Label(root, text="Last Block Creation Time - {}".format(0))
    # lable_last_blk_time['font'] = font_size

    #
    # lable_blk_time = Label(root, text="Average Block Creation Time - {}".format(0))
    # lable_blk_time['font'] = font_size
    #
    # lable_num_blk.grid(row=0, column=0, sticky=W)
    # lable_last_blk_time.grid(row=1, column=0, sticky=W)
    # lable_blk_time.grid(row=2, column=0, sticky=W)
    #
    # helv36 = tk_font.Font(family='Helvetica', size=20, weight=tk_font.BOLD)
    # transaction_b = Button(root, text="Add Transaction", font=helv36)
    # # transaction_b['font'] = font_size
    # transaction_b.grid(row=3, column=1)

    # frame = tk.Frame(root, bg="white")
    # frame.place(relwidth=0.9, relheight=0.9, relx=0.05, rely=0.05)
    #
    # lable_num_blk = tk.Label(frame, text="Number of blocks - {}".format(0))
    # lable_num_blk['font'] = font_size
    # lable_num_blk.grid(row=0, column=0, sticky=W)
    # lable_num_blk.pack()
    #
    # lable_last_blk_time = tk.Label(frame, text="Last Block Creation Time - {}".format(0))
    # lable_last_blk_time['font'] = font_size
    # lable_last_blk_time.pack()
    #
    # lable_blk_time = tk.Label(frame, text="Average Block Creation Time - {}".format(0))
    # lable_blk_time['font'] = font_size
    # lable_blk_time.pack()


