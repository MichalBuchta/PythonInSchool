def delitelnost3(n):
    for n in range(10):
        if n % 3 == 0:
            print(n, "delitelny cislem 3")
        else:
            print(n,"nedelitelny cislem 3")
delitelnost3(9)