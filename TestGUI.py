from tkinter import *
from tkinter.ttk import *


def get_acc():
    value = acc_info_ent.get()
    if test_input(value):
        temp = "\nAccount: {}".format(value)
        large_text.delete('1.0', END)
        large_text.insert(INSERT, temp)

    acc_info_ent.delete(0, END)
    return

def get_blk():
    value = blk_info_ent.get()
    if test_input(value):
        temp = "\nBlock Number: {}".format(value)
        large_text.delete('1.0', END)
        large_text.insert(INSERT, temp)

    blk_info_ent.delete(0, END)
    return

def test_input(value):
    if not str(value):
        large_text.delete('1.0', END)
        large_text.insert(INSERT, "No value was Entered!\nPlease enter a integer value!")
        return False
    elif not test_int(value):
        temp = "\"{}\" is not a valid Input\nYou can only enter an integer!\nPlease enter a integer!".format(value)
        large_text.delete('1.0', END)
        large_text.insert(INSERT, temp)
        return False
    else:
        return True

def test_int(value):
    try:
        i = int(value)
    except:
        return False
    return True

def transaction_gui():
    t_gui = Tk()
    t_gui.title("Enter a Transaction")
    heading_img = PhotoImage(file=r"images/airgeadcrypto.png")
    heading = heading_img.subsample(5, 5)

    Label(master, image=heading).grid(row=0, column=0,
                                   columnspan=2, rowspan=2, padx=0, pady=0, sticky=W + E + N + S)

    title_l = Label(t_gui, text="Create a New Block Transaction:", anchor=CENTER)
    title_l.grid(row=1, column=0, pady=2, padx=2, columnspan=2)
    # title_e = Entry(t_gui)
    # title_e.grid(row=1, column=1, sticky=W, pady=2, padx=2)

    from_acc_l = Label(t_gui, text="From Account:")
    from_acc_l.grid(row=2, column=0, sticky=W, pady=2, padx=2)
    from_acc_e = Entry(t_gui)
    from_acc_e.grid(row=2, column=1, sticky=W, pady=2, padx=2)

    to_acc_l = Label(t_gui, text="To Account:")
    to_acc_l.grid(row=3, column=0, sticky=W, pady=2, padx=2)
    to_acc_e = Entry(t_gui)
    to_acc_e.grid(row=3, column=1, sticky=W, pady=2, padx=2)

    amount_l = Label(t_gui, text="Enter Transaction Amount:")
    amount_l.grid(row=4, column=0, sticky=W, pady=2, padx=2)
    amount_e = Entry(t_gui)
    amount_e.grid(row=4, column=1, sticky=W, pady=2, padx=2)

    trans_l = Label(t_gui, text="Enter Transaction Details:", anchor=CENTER)
    trans_l.grid(row=5, column=0, pady=2, padx=2, columnspan=2)
    trans_text = Text(t_gui, height=6, width=45)
    trans_text.grid(row=6, column=0, pady=2, padx=2, rowspan=3, columnspan=2, sticky=W)

    submit_b = Button(t_gui, text="Submit")
    submit_b.grid(row=9, column=0, pady=2, padx=2, columnspan=2, sticky=W + E + N + S)



    mainloop()







# creating main tkinter window/toplevel
master = Tk()
master.title("Airgead Crypto")


# adding image (remember image should be PNG and not JPG)
img = PhotoImage(file=r"images/airgeadcrypto.png")
img2 = img.subsample(5, 5)

# setting image with the help of label
Label(master, image=img2).grid(row=0, column=0,
                               columnspan=3, rowspan=1, padx=0, pady=0, sticky=W+E+N+S)

# this will create a label widget
l1 = Label(master, text="Number of Blocks:")
l2 = Label(master, text="Creation time of last Block:")
l3 = Label(master, text="Average Block Creation time:")
l4 = Label(master, text="Add New Transaction(Block):")
l5 = Label(master, text="Display Block details:")
l6 = Label(master, text="Display Account details:")


# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row=2, column=0, sticky=W, pady=2, padx=2)
l2.grid(row=3, column=0, sticky=W, pady=2, padx=2)
l3.grid(row=4, column=0, sticky=W, pady=2, padx=2)
l4.grid(row=1, column=0, sticky=W, pady=2, padx=2)
l5.grid(row=5, column=0, sticky=W, pady=2, padx=2)
l6.grid(row=6, column=0, sticky=W, pady=2, padx=2)

# entry widgets, used to take entry from user
num_blk_ent = Entry(master)
last_time_ent = Entry(master)
avg_time_ent = Entry(master)
blk_info_ent = Entry(master)
acc_info_ent = Entry(master)

# this will arrange entry widgets
button_trans = Button(master, text="Create a new transaction(Block)", command=transaction_gui)
button_trans.grid(row=1, column=0, columnspan=2, sticky=W, padx=2)

num_blk_ent.grid(row=2, column=1, pady=2)
last_time_ent.grid(row=3, column=1, pady=2)
avg_time_ent.grid(row=4, column=1, pady=2)
blk_info_ent.grid(row=5, column=1, pady=2)
acc_info_ent.grid(row=6, column=1, pady=2)

button_blk = Button(master, text="Submit", command=get_blk)
button_acc = Button(master, text="Submit", command=get_acc)

# arranging button widgets
button_blk.grid(row=5, column=2, sticky=W)
button_acc.grid(row=6, column=2, sticky=W)

large_text = Text(master, height=10, width=55)
large_text.grid(row=7, column=0, pady=2, padx=2, columnspan=3, sticky=W)
large_text.insert(INSERT, "HI")


# checkbutton widget
# c1 = Checkbutton(master, text="Preserve")
# c1.grid(row=6, column=0, sticky=W, columnspan=2)

# # adding image (remember image should be PNG and not JPG)
# img = PhotoImage(file=r"images/ac_logo.png")
# img1 = img.subsample(3, 3)
#
# # setting image with the help of label
# Label(master, image=img1).grid(row=0, column=2,
#                                columnspan=2, rowspan=2, padx=5, pady=5)

# button widget
# b1 = Button(master, text="Zoom in")
# b2 = Button(master, text="Zoom out")
#
# # arranging button widgets
# b1.grid(row=10, column=2, sticky=W)
# b2.grid(row=10, column=3, sticky=W)

# infinite loop which can be terminated
# by keyboard or mouse interrupt
mainloop()