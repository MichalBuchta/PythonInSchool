points = 0

range2 = range(21, 30)
range3 = range(11, 20)
range4 = range(6, 10)
range5 = range(0, 5)
def get_mark(points, bonus = 0):
    if bonus != 0:
        points += bonus
    if points >= 31:
        print("1")
    elif points in range2:
        print("2")
    elif points in range3:
        print("3")
    elif points in range4:
        print("4")
    elif points in range5:
        print("5")
get_mark(20)