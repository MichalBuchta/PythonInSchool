import random
import sys
sys.setrecursionlimit(10000)
def rodnecislo():
    rand = str(random.choice('0123456789'))
    rand2 = str(random.choice('0123456789'))
    rand3 = str(random.choice('0123456789'))
    rand4 = str(random.choice('0123456789'))
    naroz = str(input("Zadej narozeni ve tvaru DDMMRRRR: "))
    day = naroz[0:2]
    month = naroz[2:4]
    year = naroz[6:8]
    day2 = int(day)
    month2 = int(month)
    year2 = int(year)

    picoina = str(year2+month2+day2)
    picovina2 = str(rand+rand2+rand3)

    celkove = str(picoina+picovina2+rand4)
    print(celkove)
    print(year,month,day,"/",rand,rand2,rand3,rand4,sep="")

    """if (celkove % 11) == 0:
        print(year,month,day,"/",rand,rand2,rand3,rand4,sep="")
    else:
        def kkk():
            rand5 = str(random.choice('0123456789'))
            if (celkove % 11) == 0:
                print(year,month,day,"/",rand,rand2,rand3,rand5,sep="")
            else:
                kkk()
        kkk()"""
        

rodnecislo()