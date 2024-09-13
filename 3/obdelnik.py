import tkinter
canvas = tkinter.Canvas()
canvas.pack()

x = int(input("zadej a: "))
y = int(input("zadej b: "))
r = str(input("zadej barvu: "))

obsah = x*y
obvod = 2*(x+y)

x2 = x+100
y2 = y+20

print("obvod: ", obvod, "cm, obsah: ", obsah, "cm")

canvas.create_rectangle(x, y, x2, y2, fill=r)
