import tkinter
root = tkinter.Tk()

root.title("Hello World!!")
root.geometry("600x500")

# create a label
my_label = tkinter.Label(root)
my_label.config(text = "Hello!", fg = "green", bg = "yellow", font = ("Wid Latin","50","italic"))
my_label.grid()

# create a label
my_label2 = tkinter.Label(root)
my_label2.config(text = "Hey there!", fg = "blue", bg = "white", font = ("Stencil", "50"), padx = "100")
my_label2.grid()

# create a label
my_label3 = tkinter.Label(root)
my_label3.config(text = "Hey you!", fg = "pink", bg = "blue", font = ("Times", "50", "bold"), pady = "30")
my_label3.grid()

root.mainloop()