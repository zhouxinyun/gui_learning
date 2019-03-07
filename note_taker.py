from tkinter import *
import Note

root = Tk()
root.title("Note Taker")
root.option_add("*font", "Consolas 20")
root.geometry("300x600")
root.config(bg="grey")


def save_note(title, body, category="Shopping"):
    print("Save Note")
    print(title)
    print(body)
    print(category)

    # new_note = Note(title, body, category)


def open_new_note():
    print("Open new note widow")
    title_value = StringVar()
    text_value = StringVar()

    new_note_window = Toplevel(root)

    new_note_title = Label(new_note_window, text="New Note")
    new_note_title.grid(sticky=E + W)

    title_label = Label(new_note_window, text="Title: ")
    title_label.grid(sticky=W, columnspan=2)

    title_entry = Entry(new_note_window, bg="grey", fg="white", textvariable=title_value)
    title_entry.grid()

    note_label = Label(new_note_window, text="Note text:")
    note_label.grid(sticky=W, columnspan=2)

    note_text = Text(new_note_window)
    note_text.config(height=10, width=20, bg="grey", fg="white")
    note_text.grid()

    button_frame = Frame(new_note_window)
    button_frame.grid()

    cancel_button = Button(button_frame, text="cancel", command=new_note_window.destroy)
    cancel_button.grid(row=0, column=1, sticky=E)

    save_button = Button(button_frame, text="save",
                         command=lambda: save_note(title_value.get(), note_text.get(1.0, END)))
    save_button.grid(row=0, column=2, sticky=E)


def open_list(list_name):
    print("Open {}".format(list_name))


title = Label(root, text="Notes")
title.config(font=("Times", "40"), width=10)
title.grid(row=0, sticky=E + W + N + S)

new_note = Button(root, text="+ New note", command=lambda: open_new_note())
new_note.config(font=("Times", "20"))
new_note.grid(row=1, sticky=W + E)

shopping = Button(root, text="Shopping List", command=lambda: open_list("Shopping List"))
shopping.config(font=("Times", "20"))
shopping.grid(row=2, sticky=W + E)

todo = Button(root, text="To Do List", command=lambda: open_list("Todo List"))
todo.config(font=("Times", "20"))
todo.grid(row=3, sticky=W + E)

homework = Button(root, text="Homework", command=lambda: open_list("Homework List"))
homework.config(font=("Times", "20"))
homework.grid(row=4, sticky=W + E)

root.mainloop()
