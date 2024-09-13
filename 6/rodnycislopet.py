def datum(birthday):
    day = birthday[0:2]
    month = birthday[2:4]
    day2 = birthday[1:2]
    month2 = birthday[3:4]
    year = birthday[4:8]
    cisla = ["01","02","03","04","05","06","07","08","09"]

    if day in cisla:
        print(day2,".",month,".",year,sep="")
    elif month in cisla:
        print(day,".",month2,".",year,sep="")
    elif day and month in cisla:
        print(day2,".",month2,".",year,sep="")
    else:
        print(day,".",month,".",year,sep="")
datum("13051968")