import tkinter
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(90, 90, 110, 110, fill='black')
canvas.create_rectangle(90, 90, 200, 200)
canvas.create_rectangle(180, 180, 200, 200, fill='black')
canvas.create_rectangle(90, 180, 110, 200, fill='black')
canvas.create_rectangle(180, 90, 200, 110, fill='black')
canvas.create_rectangle(110, 110, 180, 180, fill='black')

