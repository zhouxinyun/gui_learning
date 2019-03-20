from tkinter import *
from time import sleep
from random import *

size = 500
root = Tk()
canvas = Canvas(root, width = size, height = size)
canvas.grid()
shapes = []
while True:
    try :
        col = choice (['pink','purple','hotpink','dodgerblue'])
        x = randint(0, size)
        y = randint(0, size)