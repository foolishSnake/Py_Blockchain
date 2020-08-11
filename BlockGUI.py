import tkinter as tk
import tkinter.font as tk_font
from tkinter import *

from tkinter.ttk import *


class BlockGUI:

    root = Tk()
    font_size = tk_font.Font(size=20)



    lable_num_blk = Label(root, text="Number of blocks - {}".format(0))
    lable_num_blk['font'] = font_size


    lable_last_blk_time = Label(root, text="Last Block Creation Time - {}".format(0))
    lable_last_blk_time['font'] = font_size


    lable_blk_time = Label(root, text="Average Block Creation Time - {}".format(0))
    lable_blk_time['font'] = font_size

    lable_num_blk.grid(row=0, column=0, sticky=W)
    lable_last_blk_time.grid(row=1, column=0, sticky=W)
    lable_blk_time.grid(row=2, column=0, sticky=W)

    helv36 = tk_font.Font(family='Helvetica', size=20, weight=tk_font.BOLD)
    transaction_b = Button(root, text="Add Transaction", font=helv36)
    # transaction_b['font'] = font_size
    transaction_b.grid(row=3, column=1)

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


    root.mainloop()