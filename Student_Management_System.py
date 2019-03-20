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
    print("Student not found")


def update_details():
    student_name = student_selector.get(ACTIVE)
    current_student = get_student(student_name)
    str_name.set("Name: " + current_student.get_name())
    str_age.set("Name: " + current_student.get_age())
    str_colour.set("Name: " + current_student.get_colour())
    str_phone.set("Name: " + current_student.get_phone())

def edit_student():
    edit_window = Toplevel(root)


root = Tk()

root.title("Manage Your Students")
root.geometry("800x600")
root.option_add("*Font", "LucidaGrande 20")

student_selector = Listbox(root, height=10)
for student in student_list:
    student_selector.insert(END, student.get_name())
student_selector.grid(row=0, column=0, rowspan=10)

update_button = Button(root, text="Update details>>", command=lambda: update_details())
update_button.grid(row=10, column=0, sticky=E + W)

edit_details = Button(root, text="Edit student details", command+lambda:edit_student())
edit_details.grid(row=4, column=1, sticky =E+W)



root.mainloop()
