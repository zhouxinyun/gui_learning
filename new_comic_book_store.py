class Comic_book:
    """ A class link to the Tkinter.
    """

    def __init__(self, name, price, sell, stock):
        """Getter function: get the comic information in the books_list.
        :param name: The title of the book which choose in books_list.
        :param price: The price of the book which choose in books_list.
        :param sell: The sell number of the book which choose in books_list.
        :param stock: The stock number of the book which choose in books_list.
        """
        self.__name = name
        self.__price = float(price)
        self.__sell = int(sell)
        self.__stock = int(stock)

    def get_name(self):
        """Getter function: gets the comic title.
        :return: the title of the comic.
        """
        return self.__name

    def get_price(self):
        """Getter function: gets the comic price.
        :return: the price of the comic.
        """
        return self.__price

    def get_sell(self):
        """ Getter function: gets the comic sell number.
        :return: the sell number of the comic.
        """
        return self.__sell

    def get_stock(self):
        """ Getter function: gets the comic stock number.
        :return: the stock number of the comic.
        """
        return self.__stock

    def set_name(self, new_name):
        """ Setting function: set and change the comic book's name.
        :param new_name: change this book's name.
        :return: cancel this edit.
        """
        # check whether new book's name have any error.
        if new_name == "" or new_name is None or type(new_name) is not str:
            print("Name should be a string")
            return
        # upload new name to books_list.
        self.__name = new_name

    def set_price(self, new_price):
        """ Setting function: set and change the comic book's price.
        :param new_price: a new price number which old price would change to.
        :return: cancel this edit.
        """
        # check new price is a positive number.
        if float(new_price) <= 0:
            messagebox.showerror("Error", "Price must be a positive number.")
            return
        self.__price = float(new_price)

    def set_sell(self, new_sell):
        """ Setting function: set and change the comic book's sell number.
        :param new_sell: a number which sell would change to.
        :return: cancel this edit.
        """
        if int(new_sell) < 0:
            messagebox.showerror("Error", "Stock and Sell must be a whole number which is >= 0.")
            print("Stock and Sell must be a whole number which is >= 0.")
            return
        self.__sell = int(new_sell)

    def set_stock(self, new_stock):
        """ Setting function: set and change the comic book's stock number.
        :param new_stock: a number which stock would change to.
        :return: cancel this edit.
        """
        if int(new_stock) < 0:
            messagebox.showerror("Error", "Stock and Sell must be a whole number which is >= 0.")
            print("Stock and Sell must be a whole number which is >= 0.")
            return
        self.__stock = int(new_stock)

    def sell_one(self):
        """ Calculate the comic number which have been sold and books leave in stock.
        Shown Error message when program is not working.
        :return: cancel this sell. Stock and sell number doesn't change.
        """
        # check the stock number and calculate.
        if int(self.__stock) > 0:
            self.__stock = int(self.__stock) - 1
            self.__sell = int(self.__sell) + 1
            print("One comic have been sold.")
            print("Sold: {}".format(self.__sell))
            print("Stock: {}".format(self.__stock))
            messagebox.showinfo("Sell", "One comic have been sold")

        # if there are no stock, the comic could not sold.
        if self.__stock <= 0:
            messagebox.showerror("Sell", "Sorry, there are 0 stock for this book")
            print("There are no stock for this book.")
            return

    def restock(self, restock):
        """Calculate the restock when we add new restock in.
        Shown Error message when program is not working.
        :param restock: restock should be type in.
        :return: cancel this restock and stock number doesn't change.
        """
        # if the restock is less than or equal to 0, the program should have an message box to show Error.
        if int(restock) <= 0:
            print("Restock must be a positive whole number.")
            messagebox.showerror("Error", "Restock must be a positive number.")
            return

        # if the restock is greater than or equal to 100, the program should have an message box to show Error.
        if int(restock) >= 100:
            print("Restock must less than 100.")
            messagebox.showerror("Error", "Restock must less than 100.")
            return

        # if the number of restock which is type in is correct, calculate the total restock.
        if 0 < int(restock) < 100:
            self.__stock += int(restock)
            print("{} comic(s) have been added.".format(int(restock)))
            messagebox.showinfo("Restock", "{} comic(s) have been added.".format(int(restock)))


from tkinter import *
from tkinter import messagebox

# this list carry all information about these comics.
books_list = []
# create the book objects for when the program is  first run.
books_list.append(Comic_book("Super Dude", 3, 0, 8))
books_list.append(Comic_book("Lizard Man", 4, 0, 12))
books_list.append(Comic_book("Water Woman", 2.5, 0, 3))


def get_book(name):
    """Getter function: Get books information in the books_list.
    :param name: choose a book from the book_list.
    :return: Get info about this book.
    """
    # choose one comic in the books_list and get its' information.
    for book in books_list:
        if book.get_name() == name:
            return book


# creates and sets up a window.
root = Tk()
root.title("Comic Book Store System")
root.geometry("600x400")
root.option_add("*Font", "LucidaGrande 20")


def details():
    """Get the comic which chosen in Listbox. Gets it's information and appear in a window.
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

    # make a label shows this book's price.
    lbl_price = Label(detail_window, text="Price ($): " + str(current_book.get_price()))
    lbl_price.grid(row=1, column=0, sticky=E + W)

    # make a label shows this book's sell number.
    lbl_sell = Label(detail_window, text="Sell: " + str(current_book.get_sell()))
    lbl_sell.grid(row=2, column=0, sticky=E + W)

    # make a label shows this book's stock number.
    lbl_stock = Label(detail_window, text="Stock: " + str(current_book.get_stock()))
    lbl_stock.grid(row=3, column=0, sticky=E + W)

    # make a close window button.
    btn_close = Button(detail_window, text="Close", command=lambda: close_window(detail_window))
    btn_close.grid(row=4, column=0, sticky=E + W)


def sell_book():
    """Sell one comic, mines 1 from stock and plus one on sell.
    """
    # get the stock and sell number from books_list.
    book_name = book_selector.get(ACTIVE)
    current_book = get_book(book_name)

    current_book.sell_one()


def stock_book():
    """Add some books in stock, added value must be a number and it is positive, it will shows error info.
    """
    # create a new window
    stock_window = Toplevel(root)
    stock_window.title("Sell One Comic")
    stock_window.option_add("*Font", "LucidaGrande 20")
    stock_window.geometry("510x150")

    # get a book's information which chosen in list box.
    book_name = book_selector.get(ACTIVE)
    current_book = get_book(book_name)

    # ask how many books added in stock.
    lbl_restock_book_text = Label(stock_window, text="How many books do you want to restock?")
    lbl_restock_book_text.grid(row=0, columnspan=2)

    str_current_restock = StringVar()

    # create an input box that only can type the number in it.
    ent_restock_number = Entry(stock_window, textvariable=str_current_restock)
    ent_restock_number.grid(row=1, columnspan=2, sticky=E + W)

    # create a button can add restock into total stock.
    btn_save = Button(stock_window, text="Save",
                      command=lambda: save(current_book, str_current_restock.get(), stock_window))
    btn_save.grid(row=3, column=0, sticky=W)

    # create a button can cancel this operating.
    btn_cancel = Button(stock_window, text="Cancel", command=lambda: close_window(stock_window))
    btn_cancel.grid(row=3, column=1, sticky=E)


def create_new_book():
    """ Create a new book in books_list.
    """
    # create a new window.
    new_book_window = Toplevel(root)
    new_book_window.title("Enrol new Book")
    new_book_window.option_add("*Font", "LucidaGrande 20")

    # ask for new book's Title.
    title = Label(new_book_window, text="Nane:")
    title.grid(row=0, column=0, sticky=E)

    # ask for new book's Price.
    price = Label(new_book_window, text="Price ($):")
    price.grid(row=1, column=0, sticky=E)

    # ask for new book's Sell.
    sell_number = Label(new_book_window, text="Sell:")
    sell_number.grid(row=2, column=0, sticky=E)

    # ask for new book's stock.
    stock_number = Label(new_book_window, text="Stock:")
    stock_number.grid(row=3, column=0, sticky=E)

    # create StringVar object to hold text in Entry object.
    str_new_name = StringVar("")
    str_new_price = StringVar("")
    str_new_sell = StringVar("")
    str_new_stock = StringVar("")
    str_error_msg = StringVar("")

    # create an input box which could type book title in it.
    ask_title = Entry(new_book_window, textvariable=str_new_name)
    ask_title.grid(row=0, column=1, sticky=E + W)

    # create an input box which could type book price in it.
    ask_price = Entry(new_book_window, textvariable=str_new_price)
    ask_price.grid(row=1, column=1, sticky=E + W)

    # create an input box which could type book sell in it.
    ask_sell = Entry(new_book_window, textvariable=str_new_sell)
    ask_sell.grid(row=2, column=1, sticky=E + W)

    # create an input box which could type book stock in it.
    ask_stock = Entry(new_book_window, textvariable=str_new_stock)
    ask_stock.grid(row=3, column=1, sticky=E + W)

    # a label shows error message.
    lbl_error = Label(new_book_window, textvariable=str_error_msg, fg="red")
    lbl_error.grid(row=4, column=0, columnspan=2, sticky=N + E + S + W)

    # create a button can save these information.
    btn_creat = Button(new_book_window, text="Create", command=lambda: create_and_close(str_new_name.get(),
                                                                                        str_new_price.get(),
                                                                                        str_new_sell.get(),
                                                                                        str_new_stock.get(),
                                                                                        new_book_window,
                                                                                        str_error_msg))
    btn_creat.grid(row=5, column=1, sticky=E)

    # create a button can close this window and cancel this edit.
    btn_close = Button(new_book_window, text="Cancel", command=lambda: close_window(new_book_window))
    btn_close.grid(row=5, column=0, sticky=W)


def delete_book(book):
    """Delete a book which chosen from books_list.
    :param book: a book which chosen currently.
    """
    # create a new window.
    delete_book_window = Toplevel(root)
    delete_book_window.title("Delete this book?")
    delete_book_window.option_add("*Font", "LucidaGrande 20")

    # rechecked delete this book.
    lbl_check = Label(delete_book_window, text="Are you sure you want to delete {}?".format(book.get_name()))
    lbl_check.grid(row=0, column=0, columnspan=2, sticky=N + E + S + W)

    # do not delete this book and destroy this window.
    btn_cancel = Button(delete_book_window, text="Cancel", command=lambda: close_window(delete_book_window))
    btn_cancel.grid(row=1, column=1, sticky=W)

    # delete this book and destroy this window.
    btn_delete_check = Button(delete_book_window, text="Delete Book",
                              command=lambda: delete_and_close(book, delete_book_window))
    btn_delete_check.grid(row=1, column=0, sticky=E)


def edit_book():
    """ Edit the book which chosen in books_list.
    """
    # create new window.
    edit_window = Toplevel(root)
    edit_window.title("Edit comic's details")
    edit_window.option_add("*Font", "LucidaGrande 20")

    # Ask the name of this book.
    lbl_title = Label(edit_window, text="Name:")
    lbl_title.grid(row=0, column=0, sticky=E)

    # Ask the price of this book.
    lbl_price = Label(edit_window, text="Price ($):")
    lbl_price.grid(row=1, column=0, sticky=E)

    # Ask the sell number  of this book.
    lbl_sell = Label(edit_window, text="Sell:")
    lbl_sell.grid(row=2, column=0, sticky=E)

    # Ask the stock number of this book.
    lbl_stock = Label(edit_window, text="Stock: ")
    lbl_stock.grid(row=3, column=0, sticky=E)

    # Get current book's information from books_list.
    book_name = book_selector.get(ACTIVE)
    current_book = get_book(book_name)

    # Upload this book's information into this window.
    str_current_name = StringVar(edit_window, current_book.get_name())
    str_current_price = StringVar(edit_window, float(current_book.get_price()))
    str_current_sell = StringVar(edit_window, int(current_book.get_sell()))
    str_current_stock = StringVar(edit_window, int(current_book.get_stock()))
    str_error_msg = StringVar("")

    # create an input box which could change book title in it.
    title = Entry(edit_window, textvariable=str_current_name)
    title.grid(row=0, column=1, sticky=E + W)

    # create an input box which could change book price in it.
    price = Entry(edit_window, textvariable=str_current_price)
    price.grid(row=1, column=1, sticky=E + W)

    # create an input box which could change book sell number in it.
    sell = Entry(edit_window, textvariable=str_current_sell)
    sell.grid(row=2, column=1, sticky=E + W)

    # create an input box which could change book stock number in it.
    stock = Entry(edit_window, textvariable=str_current_stock)
    stock.grid(row=3, column=1, sticky=E + W)

    # a label shows error message.
    lbl_error = Label(edit_window, textvariable=str_error_msg, fg="red")
    lbl_error.grid(row=4, column=0, columnspan=2, sticky=N + E + S + W)

    # create a button can save these changes.
    btn_save = Button(edit_window, text="Save", command=lambda: save_and_close(current_book,
                                                                               str_current_name.get(),
                                                                               str_current_price.get(),
                                                                               str_current_sell.get(),
                                                                               str_current_stock.get(),
                                                                               edit_window,
                                                                               str_error_msg))
    btn_save.grid(row=5, column=1, sticky=E)

    # create a button can cancel these changes and back to the main window.
    btn_close = Button(edit_window, text="Cancel", command=lambda: close_window(edit_window))
    btn_close.grid(row=5, column=0, sticky=W)


def update_book_selector():
    """ Delete the old information and add new info to books list.
    """
    # Choose a book from the Listbox.
    book_selector.delete(0, END)
    for book in books_list:
        book_selector.insert(END, book.get_name())


def close_window(window):
    """A program that can close current window.
    :param window: Current window.
    """
    window.destroy()


def save(book, restock, window):
    """Check whether new restock value is a number, and add it into old stock number. Shows error information.
    :param book: Current book which chosen in books_list.
    :param restock: The value which type into the input box.
    :param window: Current window.
    :return: Add restock in to old stock.
    """
    # check whether new restock is a number.
    try:
        book.restock(int(restock))
    except ValueError:
        print("Restock must be a whole number.")
        messagebox.showerror("Error", "Restock must be a number.")
        return
    except TypeError:
        print("Error")
        messagebox.showerror("Error", "Error")
        return
    # destroy stock_window.
    close_window(window)


def save_and_close(book, new_name, new_price, new_sell, new_stock, window, error):
    """ Check the blank box and show error if typed value have and ValueError or TypeError.
    :param book: Current book which chosen in books_list.
    :param new_name: Change this book's name.
    :param new_price: Change this book's price.
    :param new_sell: Change this book's sell.
    :param new_stock: Change this book's stock.
    :param window: Current window.
    :param error: Show error message.
    :return: Upload information into books_list.
    """
    # check whether any blank box.
    if "" in [new_name, new_price, new_sell, new_stock]:
        error.set("No field can be blank.")
        print("No field can be blank.")
        return
    # upload new_name to self.__name.
    book.set_name(new_name)
    # check ValueError and TypeError of new_price, new_sell, and new_stock.
    try:
        book.set_price(new_price)
        book.set_sell(new_sell)
        book.set_stock(new_stock)
    except ValueError:
        error.set("Price, Stock and Sell must be a number.")
        print("Price, Stock and Sell must be a number.")
        return
    except TypeError as err:
        error.set(err)
        print(err)
        return

    # upload this book's information into books_list.
    update_book_selector()
    update_details()
    # destroy current window.
    close_window(window)


def create_and_close(new_name, new_price, new_sell, new_stock, window, error):
    """ Create a new book in books_list and add it's information in books_list.
    :param new_name: New book's title.
    :param new_price: New book's price.
    :param new_sell: The number of new book have been sold.
    :param new_stock: The number of new book's stock.
    :param window: The current window.
    :param error: Shows error message when program gets wrong.
    :return: Add new book's info into books_list.
    """
    # check if any blank info, shows error message.
    if "" in [new_name, new_price, new_sell, new_stock]:
        error.set("No field can be blank.")
        print("No field can be blank.")
        return

    # check price, sell and stock be a number, shows error message.
    try:
        book = Comic_book(new_name, float(new_price), int(new_sell), int(new_stock))
    except ValueError:
        error.set("Price, Stock and Sell must be a number.")
        print("Price, Stock and Sell must be a number.")
        return
    except TypeError as err:
        error.set(err)
        print(err)
        return

    # check if price, sell number and stock number be a positive number, shows error message.
    if float(new_price) <= 0:
        error.set("Price must be a positive number.")
        print("Price must be a positive number.")
        return
    elif int(new_sell) < 0 or int(new_stock) < 0:
        error.set("Stock and Sell must be a whole number which is >= 0.")
        print("Stock and Sell must be a whole number which is >= 0.")
        return

    # add information into books_list.
    books_list.append(book)
    update_book_selector()
    # destroy current window.
    close_window(window)


def delete_and_close(book, window):
    """Delete this book from books_list include this book's information.
    :param book: a book which chosen in books_list.
    :param window: Current window.
    """
    # remove selected book.
    books_list.remove(book)
    del book
    update_book_selector()
    # info shows delete successful.
    messagebox.showinfo("Success", "This book have been delete")
    # destroy current window.
    close_window(window)


def update_details():
    """ Upload new book's information into books_list.
    """
    # choose one comic in books_list and get its information.
    book_name = book_selector.get(ACTIVE)
    current_book = get_book(book_name)

    # StringVars show different information.
    str_name = StringVar(value="Title: ")
    str_price = StringVar(value="Price ($): ")
    str_sell = StringVar(value="Sell: ")
    str_stock = StringVar(value="Stock: ")

    # put this book's information in each StringVar.
    str_name.set("Title: " + current_book.get_name())
    str_price.set("Price ($): " + str(current_book.get_price()))
    str_sell.set("Sell: " + str(current_book.get_sell()))
    str_stock.set("Stock: " + str(current_book.get_stock()))


# make a list box that can choose different books.
book_selector = Listbox(root, height=12)
# get the information of this book which selected.
update_book_selector()
book_selector.grid(row=0, column=0, rowspan=7)

for book in books_list:
    book_selector.insert(END)
book_selector.grid()

# create button can shows detail window.
btn_detail = Button(root, text="DETAIL", fg="black", command=lambda: details())
btn_detail.grid(row=0, column=1, sticky=E + W)

# create button can shows sell books window, it also can mines stock, add sell number.
btn_sell = Button(root, text="SELL ONE COMIC", fg="black", command=lambda: sell_book())
btn_sell.grid(row=1, column=1, sticky=E + W)

# create button can shows restock books window, it also can calculate total stock  number.
btn_restock = Button(root, text="RESTOCK COMIC", fg="black", command=lambda: stock_book())
btn_restock.grid(row=2, column=1, sticky=E + W)

btn_edit = Button(root, text="EDIT THIS BOOK", fg="black", command=lambda: edit_book())
btn_edit.grid(row=3, column=1, sticky=E + W)

# create button can added new book in the books_list, which is include new book's information.
btn_new_book = Button(root, text="CREATE NEW BOOK", fg="black",
                      command=lambda: create_new_book()).grid(row=4, column=1, sticky=N + E + S + W)

# create button can delete current book in the books_list, include this book's information.
btn_delete = Button(root, text="DELETE THIS BOOK", fg="black",
                    command=lambda: delete_book(get_book(book_selector.get(ACTIVE))))
btn_delete.grid(row=5, column=1, sticky=E + W)

# create button can close comic_book_store system.
btn_exit = Button(root, text="EXIT", fg="black", command=lambda: close_window(root))
btn_exit.grid(row=6, column=1, sticky=E + W)

root.mainloop()
