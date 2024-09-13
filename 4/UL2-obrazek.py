import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(80, 80, 100, 100, fill='blue')
canvas.create_rectangle(90, 90, 110, 110, fill='yellow')
canvas.create_rectangle(110, 80, 130, 100, fill='black')
canvas.create_rectangle(140, 80, 160, 100, fill='red')
canvas.create_rectangle(130, 90, 150, 110, fill='green')

