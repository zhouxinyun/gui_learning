from tkinter import StringVar


class MyStudent:
    def __init__(self, name, age, phone, favourite_colour):
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__favourite_colour = favourite_colour
        self.__enrolled = True

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def add_one_year(self):
        print("Current age: ", self.__age)
        self.__age += 1
        print("New age: ", self.__age)

    def get_phone(self):
        return self.__phone

    def get_colour(self):
        return self.__favourite_colour

    def get_enrolment_status(self):
        return self.__enrolled

    def enrol(self):
        self.__enrolled = False

    def set_name(self, new_name):
        if new_name == "" or new_name is None or type(new_name) is not str:
            print("Name should be a string")
            return
        self.__name = new_name

    def set_age(self, new_age):
        if new_age is None or type(new_age) is not int:
            print("Age must be an integer")
            return
        if new_age <= 0:
            print("Age must be positive number.")
            return
        self.__age = new_age

    def set_favourite_colour(self, new_favourite_colour):
        if new_favourite_colour == "" or new_favourite_colour is None or type(new_favourite_colour) is not str:
            print("Colour must be a string")
            return
        self.__favourite_colour = new_favourite_colour

    def print_details(self):
        print("Name: ", self.__name)
        print("Age: ", self.__age)
        print("Phone Number: ", self.__phone)
        print("Favourite colour: ", self.__favourite_colour)

        if self.__enrolled:
            print("Enrolment status: enrolled.")

        else:
            print("Enrolment status: not enrolled.")


from tkinter import *

student_list = []
student_list.append(MyStudent("Jacqui", 68, "0800dominos", "purple"))
student_list.append(MyStudent("Zara", 34, "1234", "red"))
student_list.append(MyStudent("Eliza", 18, "47325", "orange"))
student_list.append(MyStudent("Hanna", 17, "384278346891", "pink"))
student_list.append(MyStudent("Lina", 5, "5678", "black"))
student_list.append(MyStudent("Cate", 12, "999999999", "yellow"))


def get_student(fname):
    for student in student_list:
        if student.get_name() == fname:
            return student
    print("Student not found")  # debug message, will print to console


root = Tk()

root.title("Manage Your Students")  # sets the title of the window
root.geometry("800x600")
root.option_add("*Font", "LucidaGrande 20")  # default font and size for every widget


def update_details():
    student_name = student_selector.get(ACTIVE)
    current_student = get_student(student_name)
    print(current_student)

    str_name.set("Name: " + current_student.get_name())
    str_age.set("Age: " + str(current_student.get_age()))
    str_phone.set("Phone: " + current_student.get_phone())
    str_colour.set("Colour: " + current_student.get_favecolour())


def close_window(window):
    window.destroy()


def save_and_close(student, new_name, new_age, new_phone, new_colour, window, error):
    student.set_name(new_name)
    try:
        student.set_age(int(new_age))
    except ValueError:
        error.set("Age must be a number")
        return
    student.set_phone(new_phone)
    student.set_favourite_colour(new_colour)
    update_student_selector()
    update_details()
    close_window(window)


def create_and_close(new_name, new_age, new_phone, new_colour, window, error):
    if "" in [new_name, new_age, new_phone, new_colour]:
        error.set("No field can be blank")
        return
    try:
        student = MyStudent(new_name, int(new_age), new_phone, new_colour)
    except ValueError:
        error.set("Age must be a whole number")
        return
    except TypeError as err:
        error.set(err)
        return
    student_list.append(student)
    update_student_selector()
    update_details()
    close_window(window)


def edit_student():
    edit_window = Toplevel(root)
    edit_window.title("Edit student details")
    edit_window.option_add("*Font", "LucidaGrande 20")

    Label(edit_window, text="Name:").grid(row=0, column=0, sticky=E)
    Label(edit_window, text="Age:").grid(row=1, column=0, sticky=E)
    Label(edit_window, text="Phone number:").grid(row=2, column=0, sticky=E)
    Label(edit_window, text="Favourite colour:").grid(row=3, column=0, sticky=E)

    student_name = student_selector.get(ACTIVE)
    current_student = get_student(student_name)

    str_current_name = StringVar(edit_window, current_student.get_name())
    str_current_age = StringVar(edit_window, str(current_student.get_age()))
    str_current_phone = StringVar(edit_window, current_student.get_phone())
    str_current_colour = StringVar(edit_window, current_student.get_favecolour())
    str_error_msg = StringVar("")

    Entry(edit_window, textvariable=str_current_name).grid(row=0, column=1, sticky=E + W)
    Entry(edit_window, textvariable=str_current_age).grid(row=1, column=1, sticky=E + W)
    Entry(edit_window, textvariable=str_current_phone).grid(row=2, column=1, sticky=E + W)
    Entry(edit_window, textvariable=str_current_colour).grid(row=3, column=1, sticky=E + W)

    Label(edit_window, textvariable=str_error_msg, fg="red").grid(row=4, column=0, columnspan=2, sticky=N + E + S + W)

    Button(edit_window, text="Cancel", command=lambda: close_window(edit_window)).grid(row=5, column=0, sticky=E)
    Button(edit_window, text="Save", command=lambda: save_and_close(current_student,
                                                                    str_current_name.get(),
                                                                    str_current_age.get(),
                                                                    str_current_phone.get(),
                                                                    str_current_colour.get(),
                                                                    edit_window,
                                                                    str_error_msg)).grid(row=5, column=1, sticky=W)


def new_student():
    new_student_window = Toplevel(root)
    new_student_window.title("Enrol new student")
    new_student_window.option_add("*Font", "LucidaGrande 20")

    Label(new_student_window, text="Name:").grid(row=0, column=0, sticky=E)
    Label(new_student_window, text="Age:").grid(row=1, column=0, sticky=E)
    Label(new_student_window, text="Phone number:").grid(row=2, column=0, sticky=E)
    Label(new_student_window, text="Favourite colour:").grid(row=3, column=0, sticky=E)

    str_new_name = StringVar("")
    str_new_age = StringVar("")
    str_new_phone = StringVar("")
    str_new_colour = StringVar("")
    str_error_msg = StringVar("")

    Entry(new_student_window, textvariable=str_new_name).grid(row=0, column=1, sticky=E + W)
    Entry(new_student_window, textvariable=str_new_age).grid(row=1, column=1, sticky=E + W)
    Entry(new_student_window, textvariable=str_new_phone).grid(row=2, column=1, sticky=E + W)
    Entry(new_student_window, textvariable=str_new_colour).grid(row=3, column=1, sticky=E + W)

    Label(new_student_window, textvariable=str_error_msg, fg="red").grid(row=4, column=0, columnspan=2,
                                                                         sticky=N + E + S + W)

    Button(new_student_window, text="Cancel", command=lambda: close_window(new_student_window)).grid(row=5, column=0,
                                                                                                     sticky=E)
    Button(new_student_window, text="Create", command=lambda: create_and_close(str_new_name.get(),
                                                                               str_new_age.get(),
                                                                               str_new_phone.get(),
                                                                               str_new_colour.get(),
                                                                               new_student_window,
                                                                               str_error_msg)).grid(row=5, column=1,
                                                                                                    sticky=W)


def delete_student(student):
    delete_student_window = Toplevel(root)
    delete_student_window.title("Delete student?")
    delete_student_window.option_add("*Font", "LucidaGrande 20")

    Label(delete_student_window, text="Are you sure you want to delete {}?".format(student.get_name())).grid(row=0,
                                                                                                             column=0,
                                                                                                             columnspan=2,
                                                                                                             sticky=N + E + S + W)
    Button(delete_student_window, text="Cancel", command=lambda: close_window(delete_student_window)).grid(row=1,
                                                                                                           column=0,
                                                                                                           sticky=E)
    Button(delete_student_window, text="Delete student",
           command=lambda: delete_and_close(student, delete_student_window)).grid(row=1, column=1, sticky=W)


def delete_and_close(student, window):
    student_list.remove(student)
    del student
    update_student_selector()
    close_window(window)


def update_student_selector():
    student_selector.delete(0, END)
    for student in student_list:
        student_selector.insert(END, student.get_name())


student_selector = Listbox(root, height=10)  # creates the listbox
# student_selector.insert(1, *student_list)          # adds all items from student_list
update_student_selector()
student_selector.grid(row=0, column=0, rowspan=10)  # puts the listbox onto the window

# the button to update the details area
update_button = Button(root, text="Update details>>", command=lambda: update_details()).grid(row=10, column=0,
                                                                                             sticky=E + W)

# variables for storing label text in
str_name: StringVar = StringVar(value="Full name: ")
str_age = StringVar(value="Age: ")
str_phone = StringVar(value="Phone: ")
str_colour = StringVar(value="Favourite colour: ")

# labels for all of the student details
full_name = Label(root, textvariable=str_name).grid(row=0, column=1, sticky=W)
age = Label(root, textvariable=str_age).grid(row=1, column=1, sticky=W)
phone_num = Label(root, textvariable=str_phone).grid(row=2, column=1, sticky=W)
fave_color = Label(root, textvariable=str_colour).grid(row=3, column=1, sticky=W)

btn_new_student = Button(root, text="Create\nnew\nstudent", bg="#99cc99", command=lambda: new_student()).grid(row=4,
                                                                                                              column=1,
                                                                                                              sticky=N + E + S + W)
btn_edit_details = Button(root, text="Edit\nstudent\ndetails", bg="#9999cc", command=lambda: edit_student()).grid(row=4,
                                                                                                                  column=2,
                                                                                                                  sticky=N + E + S + W)
btn_delete_student = Button(root, text="Delete\nstudent", bg="#cc9999", command=lambda: delete_student(get_student(
    student_selector.get(ACTIVE)))).grid(row=4, column=3, sticky=N + E + S + W)

root.mainloop()
