import tkinter as tk
from tkinter.ttk import *
import tkinter.font as tk_font
from tkinter import *




class BlockGUI:

    def dashboard(self):

        root = Tk()
        root.title("Airgead Crypto Dashboard")
        font_size = tk_font.Font(size=20)

        heading_img = PhotoImage(file=r"images/airgeadcrypto.png")
        heading = heading_img.subsample(2, 5)

        image_frame = Frame(root)
        image_frame.grid(row=0, column=0, columnspan=4, rowspan=2)
        lable_image = Label(image_frame, image=heading)
        lable_image.grid(row=0, column=0, columnspan=4, rowspan=2, sticky=W)

        parent_frame = Frame(root)
        parent_frame.grid(row=3, column=0, padx=2, pady=2)


        top_frame = Frame(parent_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        top_frame.grid(row=2, column=0, columnspan=4, rowspan=2, pady=2)

        lable_top1 = Label(top_frame, text="Mining Difficulty:", anchor="center")
        lable_top1.grid(row=0, column=0, padx=3)
        entry_top1 = Entry(top_frame)
        entry_top1.grid(row=1, column=0, sticky=W+E, padx=3, pady=2)

        lable_top2 = Label(top_frame, text="Number of Blocks:", anchor="center")
        lable_top2.grid(row=0, column=1, padx=3)
        entry_top2 = Entry(top_frame)
        entry_top2.grid(row=1, column=1, sticky=W+E, padx=3, pady=2)

        lable_top3 = Label(top_frame, text="Creation time of last Block:", anchor="center")
        lable_top3.grid(row=0, column=2, padx=3)
        entry_top3 = Entry(top_frame)
        entry_top3.grid(row=1, column=2, sticky=W+E, padx=3, pady=2)

        lable_top4 = Label(top_frame, text="Average Block Creation time:", anchor="center")
        lable_top4.grid(row=0, column=3, padx=3)
        entry_top4 = Entry(top_frame)
        entry_top4.grid(row=1, column=3, sticky=W+E, padx=3, pady=2)

        large_frame = Frame(parent_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        large_frame.grid(row=4, column=0, padx=2, columnspan=4, pady=2)

        info_frame = Frame(large_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        info_frame.grid(row=0, column=0, columnspan=2, padx=3, pady=3)

        acc_button = Button(info_frame, text="Display Account details:")
        acc_button.grid(row=0, column=0, padx=2, pady=2, sticky="ew")
        acc_entry =Entry(info_frame)
        acc_entry.grid(row=0, column=1, padx=2, pady=2)

        blk_button = Button(info_frame, text="Display Block details:")
        blk_button.grid(row=1, column=0, padx=2, pady=2, sticky="ew")
        blk_entry = Entry(info_frame)
        blk_entry.grid(row=1, column=1, padx=2, pady=2)

        mining_button = Button(info_frame, text="Set Mining difficulty")
        mining_button.grid(row=2, column=0, padx=2, pady=2, sticky="ew")
        mining_entry = Entry(info_frame)
        mining_entry.grid(row=2, column=1, padx=2, pady=2)

        output_text = Text(info_frame, height=10, width=34)
        output_text.grid(row=3, column=0,columnspan=2, padx=2,pady=2)

        transaction_frame = Frame(large_frame, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        transaction_frame.grid(row=0, column=3, columnspan=2, padx=3, pady=3)

        title_l = Label(transaction_frame, text="Create a New Block Transaction:", anchor=CENTER)
        title_l.grid(row=0, column=0, pady=2, padx=2, columnspan=2)
        # title_e = Entry(t_gui)
        # title_e.grid(row=1, column=1, sticky=W, pady=2, padx=2)

        from_acc_l = Label(transaction_frame, text="From Account:")
        from_acc_l.grid(row=1, column=0, sticky=W, pady=2, padx=2)
        from_acc_e = Entry(transaction_frame)
        from_acc_e.grid(row=1, column=1, sticky=W, pady=2, padx=2)

        to_acc_l = Label(transaction_frame, text="To Account:")
        to_acc_l.grid(row=2, column=0, sticky=W, pady=2, padx=2)
        to_acc_e = Entry(transaction_frame)
        to_acc_e.grid(row=2, column=1, sticky=W, pady=2, padx=2)

        amount_l = Label(transaction_frame, text="Enter Transaction Amount:")
        amount_l.grid(row=3, column=0, sticky=W, pady=2, padx=2)
        amount_e = Entry(transaction_frame)
        amount_e.grid(row=3, column=1, sticky=W, pady=2, padx=2)

        trans_l = Label(transaction_frame, text="Enter Transaction Details:", anchor=CENTER)
        trans_l.grid(row=4, column=0, pady=2, padx=2, columnspan=2)
        trans_text = Text(transaction_frame, height=6, width=34)
        trans_text.grid(row=5, column=0, pady=2, padx=2, rowspan=3, columnspan=2, sticky=W)

        submit_b = Button(transaction_frame, text="Submit")
        submit_b.grid(row=8, column=0, pady=2, padx=2, columnspan=2, sticky=W + E + N + S)


        root.mainloop()

run = BlockGUI()
run.dashboard()

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


