class Note:
    def __init__(self, title, text, category):
        self.__title = title
        self.__text = text
        self.__category = category

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_category(self):
        return self.__category


from tkinter import *

root = Tk()
root.title("Note Taker")
root.option_add("*font", "Consolas 20")
root.geometry("300x600")
root.config(bg="grey")

notes = []


def save_note(window, title, body, category="Shopping"):
    print("Save Note")
    print(title)
    print(body.strip())
    print(category)

    new_note = Note(title.title().strip(),
                    body.title().strip(),
                    category.title().strip())
    notes.append(new_note)
    print("Title: {}".format(new_note.get_title()))
    print("Body: {}".format(new_note.get_text()))
    print("Category: {}".format(new_note.get_category()))
    window.destroy()


def open_new_note():
    print("Open new note widow")
    title_value = StringVar()
    text_value = StringVar()

    new_note_window = Toplevel(root)

    new_note_title = Label(new_note_window, text="New Note")
    new_note_title.grid(sticky=E + W)

    title_label = Label(new_note_window, text="Title: ")
    title_label.grid(sticky=W, columnspan=2)

    title_entry = Entry(new_note_window, bg="grey", fg="white",
                        textvariable=title_value)
    title_entry.grid()

    note_label = Label(new_note_window, text="Note text:")
    note_label.grid(sticky=W, columnspan=2)

    note_text = Text(new_note_window)
    note_text.config(height=10, width=20, bg="grey", fg="white")
    note_text.grid()

    button_frame = Frame(new_note_window)
    button_frame.grid()

    cancel_button = Button(button_frame, text="cancel",
                           command=new_note_window.destroy)
    cancel_button.grid(row=0, column=1, sticky=E)

    save_button = Button(button_frame,
                         text="Save",
                         command=lambda: save_note(new_note_window,
                                                   title_value.get(),
                                                   note_text.get(1.0, END)))
    save_button.grid(row=0, column=2, sticky=E)


def open_list(list_name):
    print("Open {} List".format(list_name))
    list_window = Toplevel(root)
    list_window.title(list_name)

    for note in notes:
        title = (note.get_title())
        body = (note.get_text())
        category = (note.get_category())
        note_text = "*{}*\n {}\n".format(title, body)
        Label(list_window, text=note_text).grid()


title = Label(root, text="Notes")
title.config(font=("Times", "40"), width=10)
title.grid(row=0, sticky=E + W + N + S)

new_note = Button(root, text="+ New note",
                  command=lambda: open_new_note())
new_note.config(font=("Times", "20"))
new_note.grid(row=1, sticky=W + E)

shopping = Button(root, text="Shopping List",
                  command=lambda: open_list("Shopping"))
shopping.config(font=("Times", "20"))
shopping.grid(row=2, sticky=W + E)

todo = Button(root, text="To Do List",
              command=lambda: open_list("To Do"))
todo.config(font=("Times", "20"))
todo.grid(row=3, sticky=W + E)

homework = Button(root, text="Homework",
                  command=lambda: open_list("Homework"))
homework.config(font=("Times", "20"))
homework.grid(row=4, sticky=W + E)

root.mainloop()
