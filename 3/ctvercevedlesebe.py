import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x = int(input("zadej a: "))

canvas.create_rectangle(80, 80, x, x)
canvas.create_rectangle(250, 80, 170, 160)
