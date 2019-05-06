class Store:
    """ A class link to the Tkinter.
    """

    def __init__(self, name, sell, restock):
        """Getter function: get the comic information in the books_list.
        :param name: The title of the book which choose in books_list.
        :param sell: The sell value of the book which choose in books_list.
        :param restock: The restock value of the book which choose in books_list.
        """
        self.__name = name
        self.__sell = sell
        self.__restock = restock

    def get_name(self):
        """Getter function: gets the comic title.
        :return: the title of the comic.
        """
        return self.__name

    def get_sell(self):
        """ Getter function: gets the comic sell value.
        :return: the sell value of the comic.
        """
        return self.__sell

    def get_restock(self):
        """Getter function: gets the comic restock value.
        :return: the restock value of the comic.
        """
        return self.__restock

    def sell_one(self):
        """ Calculate the comic number which have been sold and books leave in restock.
        Shown Error message when program is not working.
        :return: If restock value is less than or equal to 0, the sell and restock don't have any changes
        """

        # check the restock value and calculate.
        if self.__restock > 0:
            self.__restock = self.__restock - 1
            self.__sell = self.__sell + 1
            print("One comic have been sold.")
            print("Sold: {}".format(self.__sell))
            print("Restock: {}".format(self.__restock))
            messagebox.showinfo("Sell", "One comic have been sold")

        # if there are no restock, the comic could not sold.
        if self.__restock <= 0:
            messagebox.showerror("Sell", "Sorry, there are 0 restock for this book")
            print("There are no restock for this book.")
            return

    def set_restock(self, new_restock):
        """Calculate the restock when we add new restock in.
        Shown Error message when program is not working.
        :param new_restock: new restock value should be type in.
        :return: If restock value is less than or equal to 0, the restock can't add in. If restock value is bigger than or equal to 100, the restock can't add in as well.
        """
        # if the value of restock which is type in is less than or equal to 0, the program should have an message box to show Error.
        if new_restock <= 0:
            print("Restock value must be a positive number.")
            messagebox.showerror("Error", "Restock value must be a positive number.")
            return

        # if the value of restock which is type in is bigger than or equal to 100, the program should have an message box to show Error.
        if new_restock >= 100:
            print("Restock must less than 100.")
            messagebox.showerror("Error", "Restock must less than 100.")
            return

        # if the value of restock which is type in is correct, calculate the total restock.
        if 0 < new_restock < 100:
            self.__restock += new_restock
            print("{} comic(s) have been added.".format(new_restock))
            messagebox.showinfo("Restock", "{} comic(s) have been added.".format(new_restock))


from tkinter import *
from tkinter import messagebox

# this list carry all information about these comics.
books_list = []
books_list.append(Store("Super Dude", 0, 8))
books_list.append(Store("Lizard Man", 0, 12))
books_list.append(Store("Water Woman", 0, 3))


def get_book(name):
    """Getter function: Get books information in the books_list.
    :param name: Choose a book when this book is in the book_list.
    :return: Get this book's information.
    """
    # choose one comic in the books_list and get its' information.
    for book in books_list:
        if book.get_name() == name:
            return book


# creates and sets up the window.
root = Tk()
root.title("Comic Book Store System")
root.geometry("600x350")
root.option_add("*Font", "LucidaGrande 20")


def details():
    """
    Get comic's information and shows them in a window.
    :return: Shows this comic book's information in this window.
    """
    # create a new window to show the comic's information.
    detail_window = Toplevel(root)
    detail_window.title("Detail")
    detail_window.option_add("*Font", "LucidaGrande 20")
    detail_window.geometry("300x200")

    # choose one comic in books_list and get its information.
    book_name = book_selector.get(ACTIVE)
    current_book = get_book(book_name)
    print("Open {} detail".format(current_book.get_name()))

    # make a label shows this book's title.
    lbl_name = Label(detail_window, text="Name: " + current_book.get_name())
    lbl_name.grid(row=0, column=0, sticky=E + W)

    # make a label shows this book's sell value.
    lbl_sell = Label(detail_window, text="Sell: " + str(current_book.get_sell()))
    lbl_sell.grid(row=1, column=0, sticky=E + W)

    # make a label shows this book's restock value.
    lbl_restock = Label(detail_window, text="Restock: " + str(current_book.get_restock()))
    lbl_restock.grid(row=2, column=0, sticky=E + W)

    # make a close window button.
    btn_close = Button(detail_window, text="Close", command=lambda: close_window(detail_window))
    btn_close.grid(row=3, column=0, sticky=E + W)


def sell_book():
    """
    Sell one comic, mines 1 from restock and plus one on sell.
    :return: Get sell value and restock value, calculate the new sell and restock value.
    """
    # get the restock and sell value from books_list.
    book_name = book_selector.get(ACTIVE)
    current_book = get_book(book_name)

    current_book.sell_one()


def restock_book():
    """
    Add some books in restock, added value must be a number and it is positive, it will shows error info.
    :return: Get old restock value and plus new restock value, get a total restock value and shown in detail window.
    """
    # creat a new window
    restock_window = Toplevel(root)
    restock_window.title("Sell One Comic")
    restock_window.option_add("*Font", "LucidaGrande 20")
    restock_window.geometry("510x150")

    # get a book's information which chosen in list box.
    book_name = book_selector.get(ACTIVE)
    current_book = get_book(book_name)

    # ask how many books added in restock.
    lbl_restock_book_text = Label(restock_window, text="How many books do you want to restock?")
    lbl_restock_book_text.grid(row=0, columnspan=2)

    str_current_restock = StringVar()

    # create an input box that only can type the number in it.
    ent_restock_value = Entry(restock_window, textvariable=str_current_restock)
    ent_restock_value.grid(row=1, columnspan=2, sticky=E + W)

    # create a button can add new restock value into total restock value.
    btn_save = Button(restock_window, text="Save",
                      command=lambda: save(current_book, str_current_restock.get(), restock_window))
    btn_save.grid(row=3, column=0)

    # create a button can cancel this operating.
    btn_cancel = Button(restock_window, text="Cancel", command=lambda: close_window(restock_window))
    btn_cancel.grid(row=3, column=1)


def delete_book(book):
    delete_book_window = Toplevel(root)
    delete_book_window.title("Delete this book?")
    delete_book_window.option_add("*Font", "LucidaGrande 20")

    Label(delete_book_window, text="Are you sure you want to delete {}?".format(book.get_name())).grid(row=0,
                                                                                                       column=0,
                                                                                                       columnspan=2,
                                                                                                       sticky=N + E + S + W)
    Button(delete_book_window, text="Cancel", command=lambda: close_window(delete_book_window)).grid(row=1,
                                                                                                     column=1,
                                                                                                     sticky=W)
    Button(delete_book_window, text="Delete Book",
           command=lambda: delete_and_close(book, delete_book_window)).grid(row=1, column=0, sticky=E)


def creat_new_book():
    new_book_window = Toplevel(root)
    new_book_window.title("Enrol new student")
    new_book_window.option_add("*Font", "LucidaGrande 20")

    Label(new_book_window, text="Name:").grid(row=0, column=0, sticky=E)
    Label(new_book_window, text="Sell:").grid(row=1, column=0, sticky=E)
    Label(new_book_window, text="Restock:").grid(row=2, column=0, sticky=E)

    str_new_name = StringVar("")
    str_new_sell = StringVar("")
    str_new_restock = StringVar("")
    str_error_msg = StringVar("")

    Entry(new_book_window, textvariable=str_new_name).grid(row=0, column=1, sticky=E + W)
    Entry(new_book_window, textvariable=str_new_sell).grid(row=1, column=1, sticky=E + W)
    Entry(new_book_window, textvariable=str_new_restock).grid(row=2, column=1, sticky=E + W)

    Label(new_book_window, textvariable=str_error_msg, fg="red").grid(row=4, column=0, columnspan=2,
                                                                      sticky=N + E + S + W)

    Button(new_book_window, text="Cancel", command=lambda: close_window(new_book_window)).grid(row=5, column=1,
                                                                                               sticky=E)
    Button(new_book_window, text="Create", command=lambda: create_and_close(str_new_name.get(),
                                                                            str_new_sell.get(),
                                                                            str_new_restock.get(),
                                                                            new_book_window,
                                                                            str_error_msg)).grid(row=5, column=0,
                                                                                                 sticky=W)


def update_book_selector():
    """
    Make a book selector that can choose a book in books_list list box.
    :return: Get this books information.
    """
    book_selector.delete(0, END)
    for book in books_list:
        book_selector.insert(END, book.get_name())


def close_window(window):
    """
    A program that can close current window.
    :param window: Current window.
    :return: Close current window.
    """
    window.destroy()


def save(book, new_restock, window):
    """
    Check whether new restock value is a number, and add it into old restock value. Shows error information.
    :param book: Current book which chosen in books_list list box.
    :param new_restock: The value which type into the input box.
    :param window: The restock_window
    :return:
    """
    # check whether new restock value is a number.
    try:
        book.set_restock(int(new_restock))
    except ValueError:
        print("Restock value must be a number.")
        messagebox.showerror("Error", "Restock value must be a number.")
    except TypeError:
        print("Error")
        messagebox.showerror("Error", "Error")
    # destroy restock_window.
    close_window(window)


def delete_and_close(book, window):
    books_list.remove(book)
    del book
    update_book_selector()
    close_window(window)


def create_and_close(new_name, new_sell, new_restock, window, error):
    if "" in [new_name, new_sell, new_restock]:
        error.set("No field can be blank.")
        print("No field can be blank.")
        return
    if int(new_sell) or int(new_restock) < 0:
        error.set("New restock value and new sell value must >= 0.")
        print("New restock value and new sell value must >= 0.")
    try:
        student = Store(new_name, int(new_sell), int(new_restock))
    except ValueError:
        error.set("Restock value and Sell value must be a whole number.")
        print("Restock value and Sell value must be a whole number.")
        return
    except TypeError as err:
        error.set(err)
        print("Error")
        return

    books_list.append(student)
    update_book_selector()
    update_details()
    close_window(window)


def update_details():
    book_name = book_selector.get(ACTIVE)
    current_book = get_book(book_name)
    print(current_book)

    str_name.set("Title: " + current_book.get_name())
    str_sell.set("Sell Value: " + str(current_book.get_sell()))
    str_restock.set("Restock Value: " + str(current_book.get_restock()))


# make a list box that can choose different books.
book_selector = Listbox(root, height=10)
# get the information of this book which selected.
update_book_selector()
book_selector.grid(row=0, column=0, rowspan=6)

for book in books_list:
    book_selector.insert(END)
book_selector.grid()

str_name = StringVar(value="Title: ")
str_sell = StringVar(value="Sell: ")
str_restock = StringVar(value="Restock: ")

# creat button can shows detail window.
btn_detail = Button(root, text="DETAIL", fg="black", command=lambda: details())
btn_detail.grid(row=0, column=1, sticky=E + W)

# creat button can shows sell books window, it also can mines restock, add sell value.
btn_sell = Button(root, text="SELL ONE COMIC", fg="black", command=lambda: sell_book())
btn_sell.grid(row=1, column=1, sticky=E + W)

# creat button can shows restock books window, it also can plus restock value.
btn_restock = Button(root, text="RESTOCK COMIC", fg="black", command=lambda: restock_book())
btn_restock.grid(row=2, column=1, sticky=E + W)

btn_new_book = Button(root, text="CREAT NEW BOOK", fg="black",
                      command=lambda: creat_new_book()).grid(row=3, column=1, sticky=N + E + S + W)

btn_delete = Button(root, text="DELETE THIS BOOK", fg="black",
                    command=lambda: delete_book(get_book(book_selector.get(ACTIVE))))
btn_delete.grid(row=4, column=1, sticky=E + W)

# create button can close comic_book_store system.
btn_exit = Button(root, text="EXIT", fg="black", command=lambda: close_window(root))
btn_exit.grid(row=5, column=1, sticky=E + W)

root.mainloop()
