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
student_list.append(MyStudent("Jacqui", 68, "0800", "purple"))
student_list.append(MyStudent("Zara", 34, "1234", "red"))
student_list.append(MyStudent("Eliza", 17, "47325", "orange"))
student_list.append(MyStudent("Hanna", 18, "55325335", "black"))
student_list.append(MyStudent("Lina", 5, "4512565", "black"))
student_list.append(MyStudent("Cate", 12, "45645453", "yellow"))
root = Tk()

root.title("Manage Your Students")
root.geometry("800x600")
root.option_add("*Font", "LucidaGrande 20")
root.config(padx=10, pady=10)

status_text = StringVar("")
status_text.set("a message")

student_selector = Listbox(root, height=10)
student_selector.grid(row=0, column=0, rowspan=10)


def update_list_students():
    for student in student_list:
        student_selector.insert(END, student.get_name())


def get_student(fname):
    for student in student_list:
        if student.get_name() == fname:
            return student
    print("Student not found")


def view_details():
    view_window = Toplevel(root)
    view_window.title("View student details")

    student_name = update_list_students().get(ACTIVE)
    current_student = get_student(student_name)

    str_name = StringVar("")
    str_name.set(current_student.get_name())
    str_age = StringVar("")
    str_age.set(current_student.get_age())
    str_phone = StringVar("")
    str_phone.set(current_student.get_phone())
    str_colour = StringVar("")
    str_colour.set(current_student.get_colour())

    full_name = Label(view_window, text="Name: ")
    full_name.grid(row=0, column=1, sticky=W)
    full_name_val = Label(view_window, textvariable=str_name)
    full_name_val.grid(row=0, column=1, sticky=W)

    age = Label(view_window, text="Age: ")
    age.grid(row=1, column=1, sticky=W)
    age_val = Label(root, textvariable=str_age)
    age_val.grid(row=1, column=1, sticky=W)

    phone_number = Label(view_window, text="Phone Number: ")
    phone_number.grid(row=2, column=1, sticky=W)
    phone_number_val = Label(root, textvariable=str_phone)
    phone_number_val.grid(row=2, column=1, sticky=W)

    colour = Label(view_window, text="Colour: ")
    colour.grid(row=3, column=1, sticky=W)
    colour_val = Label(root, textvariable=str_colour)
    colour_val.grid(row=3, column=1, sticky=W)


def new_student():
    new_window = Toplevel(root)
    new_window.title("New student")


def remove_student():
    pass


btn_view_details = Button(root, text="View student details", command=lambda: view_details(), width=20)
btn_view_details.grid(row=4, column=1, sticky=E + W, padx=10)
update_button = Button(root, text="Update details >>").grid(row=10, column=0, sticky=E + W)

root.mainloop()
